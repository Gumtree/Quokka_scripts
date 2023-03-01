from java.lang import System
import time
import math
from gumpy.vis.event import MouseListener, MaskEventListener, AWTMouseListener
from gumpy.nexus.fitting import Fitting, GAUSSIAN_FITTING
from gumpy.commons.logger import n_logger
from gumpy.commons import sics
from Internal import sicsext
from java.lang import Double
from java.io import File
from copy import copy
# Script control setup area
# script info
__script__.title = 'GSOM Alignment'
__script__.version = ''
#pact = Act('previous_step()', '<- Previous Step')

SAVED_MASK_PRFN = 'quokka.savedMasks'
SAVED_INC_MASK_PRFN = 'quokka.savedIncMasks'
SAVED_EXC_MASK_PRFN = 'quokka.savedExcMasks'

class RegionEventListener(MaskEventListener):
    
    def __init__(self):
        MaskEventListener.__init__(self)
    
    def mask_added(self, mask):
        pass
            
    def mask_removed(self, mask):
        global DS
        update_mask_list()
        process(DS)
    
    def mask_updated(self, mask):
        global __mask_updated__
        update_mask_list()
        __mask_updated__ = True
        
regionListener = RegionEventListener()

class MousePressListener(AWTMouseListener):
    def __init__(self):
        AWTMouseListener.__init__(self)
    
    def mouse_released(self, event):
        global __mask_updated__
        global DS
        if __mask_updated__ :
            process(DS)
            __mask_updated__ = False
    
mouse_press_listener = MousePressListener()

__inc_masks__ = []
__exc_masks__ = []

def load_mask_prof():
    global __inc_masks__, __exc_masks__, SAVED_INC_MASK_PRFN, \
            SAVED_EXC_MASK_PRFN, SAVED_MASK_PRFN
    s_mask = get_prof_value(SAVED_MASK_PRFN)
    if not s_mask is None and s_mask.strip() != '':
        reg_list.value = s_mask
    reg_list.title = 'mask list'
    reg_list.enabled = False
    inc_masks = get_prof_value(SAVED_INC_MASK_PRFN)
    if not inc_masks is None and inc_masks.strip() != '':
        __inc_masks__ = eval(inc_masks)
    exc_masks = get_prof_value(SAVED_EXC_MASK_PRFN)
    if not exc_masks is None and exc_masks.strip() != '':
        __exc_masks__ = eval(exc_masks)

def save_mask_prof():
    global __inc_masks__, __exc_masks__, SAVED_EXC_MASK_PRFN, \
            SAVED_INC_MASK_PRFN, SAVED_MASK_PRFN
    set_prof_value(SAVED_MASK_PRFN , str(reg_list.value))
    set_prof_value(SAVED_INC_MASK_PRFN , str(__inc_masks__))
    set_prof_value(SAVED_EXC_MASK_PRFN , str(__exc_masks__))
    save_pref()
    
def update_mask_list():
    if Plot3.ndim > 0:
        reg_list.value = mask2str(Plot3.get_masks())
        inte_masks(Plot3.ds, Plot3.get_masks())
        
def inte_masks(ds, masks):
    global __inc_masks__
    global __exc_masks__
    __inc_masks__ = []
    __exc_masks__ = []
    x_axis = ds.axes[-1]
    y_axis = ds.axes[-2]

    for mask in masks:
        y_iMin = int((mask.minY - y_axis[0]) / (y_axis[-1] - y_axis[0]) \
                     * (y_axis.size - 1))
        if y_iMin < 0 :
            y_iMin = 0
        if y_iMin >= y_axis.size:
            continue
        y_iMax = int((mask.maxY - y_axis[0]) / (y_axis[-1] - y_axis[0]) \
                     * (y_axis.size - 1)) + 1
        if y_iMax < 0:
            continue
        x_iMin = int((mask.minX - x_axis[0]) / (x_axis[-1] - x_axis[0]) \
                     * (x_axis.size - 1))
        if x_iMin < 0:
            x_iMin = 0;
        if x_iMin >= x_axis.size:
            continue
        x_iMax = int((mask.maxX - x_axis[0]) / (x_axis[-1] - x_axis[0]) \
                     * (x_axis.size - 1)) + 1
        if x_iMax < 0:
            continue
        if mask.isInclusive() :
            __inc_masks__.append([x_iMin, x_iMax, y_iMin, y_iMax])
        else:
            __exc_masks__.append([x_iMin, x_iMax, y_iMin, y_iMax])

def str2maskstr(value):
    items = value.split(';')
    res = []
    for item in items:
        name = item[0:item.index('[')];
        rstr = item[item.index('[') + 1 : item.index(']')]
        range = rstr.split(',')
        range.append(name)
        res.append(range)
    return res

def str2mask(value):
    items = value.split(';')
    masks = []
    for item in items:
        name = item[0:item.index('[')];
        rstr = item[item.index('[') + 1 : item.index(']')]
        range = rstr.split(',')
        mask = RectangleMask(True, float(range[0]), float(range[2]), \
                             float(range[1]) - float(range[0]), \
                             float(range[3]) - float(range[2]))
        mask.name = name
        masks.append(mask)
    return masks

def mask2str(masks):
    res = ''
    for mask in masks:
        res += mask.name
        res += '[' + str(mask.minX) + ',' + str(mask.maxX) + ',' \
                + str(mask.minY) + ',' + str(mask.maxY) + ']'
        if masks.indexOf(mask) < len(masks) - 1:
            res += ';'
    return res

def add_dataset(f):
    global __DATASOURCE__
    try:
        print(str(f))
        __DATASOURCE__.removeDataset(str(f))
        __DATASOURCE__.addDataset(str(f), False)
    except:
        print 'error in adding dataset: ' + f

DS = None

G1 = Group('Scan on gsom')
device_name = Par('string', 'gsom', options = ['gsom', 'dummy_motor'], 
                  command = 'update_axis_name()')
sample_name = Par('string', '')
scan_start = Par('float', 0)
scan_stop = Par('float', 0)
number_of_points = Par('int', 0)
scan_mode = Par('string', 'time', options = ['time', 'count'])
scan_mode.enabled = True
scan_preset = Par('int', 0)
act1 = Act('scan_device()', 'Scan on Device')
def scan_device():
    aname = device_name.value
    try:
        if DEBUGGING :
            aname = 'dummy_motor'
    except:
        pass
    axis_name.value = aname
    slog('runscan ' + str(device_name.value) + ' ' + str(scan_start.value) + ' ' + str(scan_stop.value) \
                    + ' ' + str(number_of_points.value) + ' ' + str(scan_mode.value) + ' ' + str(scan_preset.value))
    sn = str(sample_name.value)
    if len(sn.strip()) > 0:
        sics.execute('samplename ' + sn.strip())
    sicsext.runscan(device_name.value, scan_start.value, scan_stop.value, number_of_points.value, 
                    scan_mode.value, scan_preset.value, load_experiment_data, True, \
                    'HISTOGRAM_XY')
    time.sleep(2)
    peak_pos.value = float('NaN')
    FWHM.value = float('NaN')
    if auto_fit.value :
        fit_curve()
    
#footer = 'POS_OF_PEAK=' + str(peak_pos.value) + '; ' \
#        + 'FWHM=' + str(FWHM.value)
#n_logger.log_plot(Plot1, footer = footer)
#ice_name.options = devices
def update_axis_name():
    axis_name.value = device_name.value
        
G1.add(device_name, sample_name, scan_start, scan_stop, number_of_points, scan_mode, scan_preset, act1)

G2 = Group('Fitting')
data_name = 'total_counts'
normalise = Par('bool', True)
axis_name = Par('string', '')
axis_name.enabled = True
auto_fit = Par('bool', False)
fit_min = Par('float', 'NaN')
fit_max = Par('float', 'NaN')
peak_pos = Par('float', 'NaN')
FWHM = Par('float', 'NaN')
fact = Act('fit_curve()', 'Fit Again')
#offset_done = Par('bool', False)
#act3 = Act('offset_s2()', 'Set Device Zero Offset')
G2.add(normalise, axis_name, auto_fit, fit_min, 
       fit_max, peak_pos, FWHM, fact)

G3 = Group('Plot 2')
allow_duplication = Par('bool', False)
act2 = Act('import_to_plot2()', text = 'Import Data Files to Plot2')
to_remove = Par('string', '', options=[])
act3 = Act('remove_curve()', 'Remove selected curve')
plot2_fit_min = Par('float', 'NaN')
plot2_fit_max = Par('float', 'NaN')
plot2_act1 = Act('plot2_fit_curve()', 'Gaussian Fit Plot2')
plot2_peak_pos = Par('float', 'NaN')
plot2_FWHM = Par('float', 'NaN')
act_reset = Act('reset_fitting_plot2()', 'Remove Fitting')
act_remove_all = Act('remove_all_curves()', 'Remove All Curves')
G3.add(allow_duplication, act2, to_remove, act3, plot2_fit_min, \
       plot2_fit_max, plot2_act1, plot2_peak_pos, plot2_FWHM, \
       act_reset, act_remove_all)

G4 = Group('Plot3')
reg_enabled = Par('bool', True)
reg_enabled.title = 'region enabled'
reg_list = Par('string', '')
G4.add(reg_enabled, reg_list)

load_mask_prof()

def scan(dname, start, stop, np, mode, preset):
    device_name.value = dname
    scan_start.value = start
    scan_stop.value = stop
    number_of_points.value = np
    scan_mode.value = mode
    scan_preset.value = preset
    axis_name.value = dname
    scan_device()
    
#def fit_curve():
#    __std_fit_curve__()

def fit_curve():
    global Plot1
    ds = Plot1.ds
    if len(ds) == 0:
        log('Error: no curve to fit in Plot1.\n')
        return
    for d in ds:
        if d.title == 'fitting':
            Plot1.remove_dataset(d)
    d0 = ds[0]
    fitting = Fitting(GAUSSIAN_FITTING)
    try:
        fitting.set_histogram(d0, fit_min.value, fit_max.value)
        val = peak_pos.value
        if val == val:
            fitting.set_param('mean', val)
        val = FWHM.value
        if val == val:
            fitting.set_param('sigma', math.fabs(val / 2.35482))
        res = fitting.fit()
        res.var[:] = 0
        res.title = 'fitting'
        Plot1.add_dataset(res)
        Plot1.pv.getPlot().setCurveMarkerVisible(Plot1.__get_NXseries__(res), False)
        mean = fitting.params['mean']
        mean_err = fitting.errors['mean']
        FWHM.value = 2.35482 * math.fabs(fitting.params['sigma'])
        FWHM_err = 5.54518 * math.fabs(fitting.errors['sigma'])
        log('POS_OF_PEAK=' + str(mean) + ' +/- ' + str(mean_err))
        log('FWHM=' + str(FWHM.value) + ' +/- ' + str(FWHM_err))
        log('Chi2 = ' + str(fitting.fitter.getQuality()))
        peak_pos.value = fitting.mean
#        print fitting.params
    except:
#        traceback.print_exc(file = sys.stdout)
        log('can not fit\n')


# This function is called when pushing the Run button in the control UI.
def __run_script__(fns):
#    __std_run_script__(fns)
    __std_run_script__(fns)

def load_experiment_data():
    global mouse_press_listener, regionListener
    basename = sicsext.getBaseFilename()
    fullname = str(System.getProperty('sics.data.path') + '/' + basename)
    df.datasets.clear()
    f = File(fullname)
    if f.exists():
        ds = df[fullname]
        add_dataset(f.getAbsolutePath())
        process(ds)
    else:
        log('file not found: ' + fullname)
#    dname = 'total_counts'
#    data = SimpleData(ds[dname])
#    axis = SimpleData(ds[str(axis_name.value)])
#    if data.size > axis.size:
#        data = data[:axis.size]
#    if normalise.value :
#        if dname == 'bm1_counts':
#            tname = 'bm1_time'
#        elif dname == 'bm2_counts':
#            tname = 'bm2_time'
#        else:
#            tname = 'detector_time'
#        norm = ds[tname]
#        if norm != None and hasattr(norm, '__len__'):
#            avg = norm.sum() / len(norm)
#            niter = norm.item_iter()
#            if niter.next() <= 0:
#                niter.set_curr(1)
#            data = data / norm * avg
#
#    ds2 = Dataset(data, axes=[axis])
#    ds2.title = ds.id
#    ds2.location = fullname
#    fit_min.value = axis.min()
#    fit_max.value = axis.max()
#    Plot1.set_dataset(ds2)
#    Plot1.x_label = axis_name.value
#    Plot1.y_label = data_name
#    Plot1.title = data_name + ' vs ' + axis_name.value
#    Plot1.pv.getPlot().setMarkerEnabled(True)
    

def intg(ds):
    if ds.ndim == 4:
        ds = ds.get_reduced(1)
    di = ds.intg(0)
    Plot3.set_dataset(di)
    if len(Plot3.get_masks()) == 0:
        if reg_list.value != None and reg_list.value.strip() != '':
            masks = str2maskstr(reg_list.value)
            for mask in masks:
                Plot3.add_mask_2d(float(mask[0]), float(mask[1]), \
                                  float(mask[2]), float(mask[3]), \
                                  mask[4], mask[4].startswith('I'))
    
def import_to_plot2():
    global Plot2, Plot1
    dss = Plot1.ds
    if len(dss) > 0:
        ds = dss[0]
        if not allow_duplication.value:
            did = str(ds.id)
            if to_remove.options.__contains__(did):
                for item in reversed(Plot2.ds) :
                    if item.title == did :
                        Plot2.remove_dataset(item)
                        rlist = copy(to_remove.options)
                        rlist.remove(did)
                        to_remove.options = rlist
                        break
#        ds2 = Dataset(data, axes=[axis])
#        ds2.title = ds.id
        Plot2.add_dataset(ds)
        Plot2.x_label = axis_name.value
        Plot2.y_label = 'total_counts'
        Plot2.title = 'Overlay'
        rlist = copy(to_remove.options)
        rlist.append(str(ds.title))
        to_remove.options = rlist

def remove_curve():
    global Plot2
    if Plot2.ds is None :
        return
    if to_remove.value is None or to_remove.value == '':
        return
    for item in Plot2.ds :
        if item.title == to_remove.value :
            Plot2.remove_dataset(item)
            rlist = copy(to_remove.options)
            rlist.remove(to_remove.value)
            to_remove.options = rlist
            break

def plot2_fit_curve():
    global Plot2
    ds = Plot2.ds
    if len(ds) == 0:
        log('Error: no curve to fit in Plot2.\n')
        return
    for d in ds:
        if d.title == 'fitting':
            Plot2.remove_dataset(d)
    if len(ds) == 1:
        sds = ds[0]
    else:
        sds = Plot2.get_selected_dataset()
        if sds is None :
            open_error('Please select a curve to fit. Right click on the plot to focus on a curve. Or use CTRL + Mouse Click on a curve to select one.')
            return
    fitting = Fitting(GAUSSIAN_FITTING)
    try:
        fitting.set_histogram(sds, plot2_fit_min.value, plot2_fit_max.value)
        val = plot2_peak_pos.value
        if val == val:
            fitting.set_param('mean', val)
        val = plot2_FWHM.value
        if val == val:
            fitting.set_param('sigma', math.fabs(val / 2.35482))
        res = fitting.fit()
        res.var[:] = 0
        res.title = 'fitting'
        Plot2.add_dataset(res)
        Plot2.pv.getPlot().setCurveMarkerVisible(Plot2.__get_NXseries__(res), False)
        mean = fitting.params['mean']
        log('POS_OF_PEAK=' + str(mean))
        log('FWHM=' + str(2.35482 * math.fabs(fitting.params['sigma'])))
        log('Chi2 = ' + str(fitting.fitter.getQuality()))
        plot2_peak_pos.value = fitting.mean
        plot2_FWHM.value = 2.35482 * math.fabs(fitting.params['sigma'])
#        print fitting.params
    except:
#        traceback.print_exc(file = sys.stdout)
        log('can not fit\n')

def reset_fitting_plot2():
    global Plot2
    ds = Plot2.ds
    if len(ds) == 0:
        return
    for d in ds:
        if d.title == 'fitting':
            Plot2.remove_dataset(d)
    plot2_peak_pos.value = Double.NaN
    plot2_FWHM.value = Double.NaN


def remove_all_curves():
    global Plot2
    Plot2.clear()
    plot2_fit_min.value = Double.NaN
    plot2_fit_max.value = Double.NaN
    plot2_peak_pos.value = Double.NaN
    plot2_FWHM.value = Double.NaN
    to_remove.options = []
    

def __dataset_added__(fns = None):
    pass
    
def process(ds):
    global Plot1, Plot2, Plot3, DS, data_name
    log('process data')
    axis_name.value = ds.axes[0].name
    if ds.ndim == 4:
        ds = ds.get_reduced(1)
    dname = 'total_counts'
    if dname == 'total_counts' and reg_enabled.value and len(__inc_masks__) + len(__exc_masks__) > 0:
        if len(__exc_masks__) > 0:
            res = copy(ds)
            for mask in __exc_masks__:
                res[:, mask[2]:mask[3], mask[0]:mask[1]] = 0
        else :
            res = copy(ds)
        if len(__inc_masks__) > 0:
            log('apply inclusive masks')
            r = dataset.instance(res.shape, dtype=int)
            for mask in __inc_masks__:
                r[:, mask[2]:mask[3], mask[0]:mask[1]] = res[:, mask[2]:mask[3], mask[0]:mask[1]]
        else :
            r = res
        data = r.sum(0)
    else:
        data = ds[dname]
    if normalise.value :
        tname = 'detector_time'
        norm = ds[tname]
        if norm != None and hasattr(norm, '__len__'):
            avg = norm.sum() / len(norm)
            niter = norm.item_iter()
            if niter.next() <= 0:
                niter.set_curr(1)
            data = data / norm * avg

    axis = ds.get_metadata(str(axis_name.value))
    if not hasattr(axis, '__len__'):
        axis = SimpleData([axis], title = (axis_name.value))
    ds2 = Dataset(data, axes=[axis])
    ds2.title = ds.id
    ds2.location = ds.location
    fit_min.value = axis.min()
    fit_max.value = axis.max()
    Plot1.set_dataset(ds2)
    Plot1.x_label = axis_name.value
    Plot1.y_label = dname
    Plot1.title = str(ds.samplename) + ' QKK%07d ' % ds.id + dname + ' vs ' + axis_name.value
    Plot1.pv.getPlot().setMarkerEnabled(True)
    peak_pos.value = float('NaN')
    FWHM.value = float('NaN')
    if auto_fit.value :
        fit_curve()
    intg(ds)
    DS = ds
    Plot3.set_awt_mouse_listener(mouse_press_listener)
    Plot3.set_mask_listener(regionListener)
    Plot3.title = 'QKK%07d integration' % ds.id
    if reg_enabled.value:
        save_mask_prof()

    
def __std_run_script__(fns):
    # Use the provided resources, please don't remove.
    global Plot1
    global Plot2
    global Plot3
    # check if a list of file names has been given
    if (fns is None or len(fns) == 0) :
        print 'no input datasets'
    else :
        if len(fns) > 0:
            fn = fns[0]
            # load dataset with each file name
#            ds = Plot1.ds
#            if ds != None and len(ds) > 0:
#                if ds[0].location == fn:
#                    return
            df.datasets.clear()
            ds = df[fn]
            
            process(ds)
            
def auto_run():
    pass

def __dispose__():
    global Plot1
    global Plot2
    global Plot3
    Plot1.clear()
    Plot2.clear()
    Plot3.clear()
