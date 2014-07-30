import math
# Script control setup area
# script info
__script__.title = 'Align Beam Stops'
__script__.version = '1.0'

DEFAULT_ATT = float('nan')
ROUGH_BSX_SCAN_START = 10
ROUGH_BSX_SCAN_STOP = 300
ROUGH_BSX_SCAN_NUMBER_OF_STEPS = 21
ROUGH_BSX_SCAN_TIME = 10

BSZ_SCAN_START = 10
BSZ_SCAN_STOP = 270
BSZ_SCAN_NUMBER_OF_STEPS = 21
BSZ_SCAN_TIME = 10

DETAIL_BSX_SCAN_WIDTH = 10
DETAIL_BSX_SCAN_NUMBER_OF_STEPS = 21
DETAIL_BSX_SCAN_TIME = 10

# Use below example to create parameters.
# The type can be string, int, float, bool, file.

att = Par('float', DEFAULT_ATT)
att.title = 'set appropriate att'
att_set = False

att_act = Act('run_att()', 'drive att')

def run_att():
    global att_set
    ac = True
    if math.isnan(att.value):
        return
    if att.value < 180:
        ac = confirm('You\'v set att to be less than 180. Please confirm that\'s what you want.')
    if ac:
          sics.drive('att', att.value)
          att_set = True
    else:
        raise Exception, 'Automatic scan cancelled'

run_all_act = Act('run_all()', 'run alignment automatically')

def run_all():
    global att_set
    if not att_set:
        open_error('Please set att first.')
        return
    run_action(g1_run)
    run_action(g2_run)
    run_action(g3_run)
    open_information('Alignment is finished')

g1_start = Par('float', ROUGH_BSX_SCAN_START)
g1_start.title = 'start'
g1_stop = Par('float', ROUGH_BSX_SCAN_STOP)
g1_stop.title = 'stop'
g1_number_of_step = Par('float', ROUGH_BSX_SCAN_NUMBER_OF_STEPS)
g1_number_of_step.title = 'number of steps'
g1_counting_time = Par('int', ROUGH_BSX_SCAN_TIME)
g1_counting_time.title = 'counting time'

# Use below example to create a button
g1_run = Act('scan_bsx()', 'run bsx scan') 
def scan_bsx():
    scan_device('bsx', g1_start, g1_stop, g1_number_of_step, g1_counting_time)
    Plot2.set_dataset(Plot1.ds[0])
    fit_curve()
    ac = confirm('The estimated bsx centre position is ' + str(peak_pos.value) \
                 + ', do you accept this estimation?')
    if ac:
        g1_estimate_x.value = peak_pos.value
        run_action(g1_drive)
    else:
        raise Exception, 'Automatic scan cancelled'
        
    
g1_estimate_x = Par('float', float('nan'))
g1_estimate_x.title = 'estimated x centre'
g1_drive = Act('drive_bsx(g1_estimate_x)', 'drive bsx to estimated centre')
def drive_bsx(centre_par):
    value = centre_par.value
    if not math.isnan(value):
        slog('drive bsx to ' + str(value))
        sics.drive('bsx', value)
        half_width = DETAIL_BSX_SCAN_WIDTH / 2.0
        start = value - half_width
        if start < 10:
            start = 10
        g3_start.value = start
        stop = value + half_width
        if stop > 270:
            stop = 270
        g3_stop.value = stop
        

g_bsx1 = Group('Scan on bsx roughly')
g_bsx1.add(g1_start, g1_stop, g1_number_of_step, \
           g1_counting_time, g1_run, g1_estimate_x, g1_drive)

g2_start = Par('float', BSZ_SCAN_START)
g2_start.title = 'start'
g2_stop = Par('float', BSZ_SCAN_STOP)
g2_stop.title = 'stop'
g2_number_of_step = Par('float', BSZ_SCAN_NUMBER_OF_STEPS)
g2_number_of_step.title = 'number of steps'
g2_counting_time = Par('int', BSZ_SCAN_TIME)
g2_counting_time.title = 'counting time'

# Use below example to create a button
g2_run = Act('scan_bsz()', 'run bsz scan') 
def scan_bsz():
    scan_device('bsz', g2_start, g2_stop, g2_number_of_step, g2_counting_time)
    Plot3.set_dataset(Plot1.ds[0])
    fit_curve()
    ac = confirm('The estimated bsz centre position is ' + str(peak_pos.value) \
                 + ', do you accept this estimation?')
    if ac:
        g2_estimate_z.value = peak_pos.value
        run_action(g2_drive)
    else:
        raise Exception, 'Automatic scan cancelled'
    
g2_estimate_z = Par('float', float('nan'))
g2_estimate_z.title = 'estimated z centre'
g2_drive = Act('drive_bsz(g2_estimate_z)', 'drive bsz to estimated centre')
def drive_bsz(centre_par):
    if not math.isnan(centre_par.value):
        slog('drive bsz to ' + str(centre_par.value))
        sics.drive('bsz', centre_par.value)

g2_bsz = Group('Scan on bsz')
g2_bsz.add(g2_start, g2_stop, g2_number_of_step, \
           g2_counting_time, g2_run, g2_estimate_z, g2_drive)

g3_start = Par('float', 0)
g3_start.title = 'start'
g3_stop = Par('float', 0)
g3_stop.title = 'stop'
g3_number_of_step = Par('float', DETAIL_BSX_SCAN_NUMBER_OF_STEPS)
g3_number_of_step.title = 'number of steps'
g3_counting_time = Par('int', DETAIL_BSX_SCAN_TIME)
g3_counting_time.title = 'counting time'

# Use below example to create a button
g3_run = Act('scan_bsx2()', 'run bsx scan again') 
def scan_bsx2():
    scan_device('bsx', g3_start, g3_stop, g3_number_of_step, g3_counting_time)
    Plot2.set_dataset(Plot1.ds[0])
    fit_curve()
    ac = confirm('The estimated bsx centre position is ' + str(peak_pos.value) \
                 + ', do you accept this estimation?')
    if ac:
        g3_estimate_x.value = peak_pos.value
        run_action(g3_drive)
    
g3_estimate_x = Par('float', float('nan'))
g3_estimate_x.title = 'estimated x centre'
g3_drive = Act('drive_bsx2(g3_estimate_x)', 'drive bsx to estimated centre')
def drive_bsx2(centre_par):
    value = centre_par.value
    if not math.isnan(value):
        slog('drive bsx to ' + str(value))
        sics.drive('bsx', value)
        
g3_bsx = Group('Scan on bsx again')
g3_bsx.add(g3_start, g3_stop, g3_number_of_step, \
           g3_counting_time, g3_run, g3_estimate_x, g3_drive)

G4 = Group('Fitting')
data_name = Par('string', 'total_counts')
axis_name = Par('string', '')
fit_min = Par('float', 'NaN')
fit_max = Par('float', 'NaN')
peak_pos = Par('float', 'NaN')
FWHM = Par('float', 'NaN')
fact = Act('fit_curve()', 'fit again')
#offset_done = Par('bool', False)
#act3 = Act('offset_s2()', 'Set Device Zero Offset')
G4.add(data_name, axis_name, fit_min, fit_max, peak_pos, FWHM, fact)

def scan_device(device_name, scan_start, scan_stop, number_of_points, scan_preset):
    axis_name.value = device_name
    slog('runscan ' + str(device_name) + ' ' + str(scan_start.value) + ' ' + str(scan_stop.value) \
                    + ' ' + str(number_of_points.value) + ' time ' + str(scan_preset.value))
    sicsext.runscan(device_name, scan_start.value, scan_stop.value, number_of_points.value, 
                    'time', scan_preset.value, load_experiment_data, True, \
                    'HISTOGRAM_XY')
    time.sleep(2)
    peak_pos.value = float('NaN')
    FWHM.value = float('NaN')
        
# Use below example to create a new Plot
# Plot4 = Plot(title = 'new plot')

def fit_curve():
    ds = Plot1.ds
    if len(ds) == 0:
        log('Error: no curve to fit in Plot1.\n')
        return
    for d in ds:
        if d.title == 'fitting':
            Plot1.remove_dataset(d)
    ds0 = ds[0]
    ds0_max = ds0.max()
    d0= ds0_max - ds0
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
        res = ds0_max - res
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


def load_experiment_data():
    basename = sicsext.getBaseFilename()
    fullname = str(System.getProperty('sics.data.path') + '/' + basename)
    df.datasets.clear()
    ds = df[fullname]
    dname = str(data_name.value)
    data = SimpleData(ds[dname])
#    data = ds[str(data_name.value)]
    axis = SimpleData(ds[str(axis_name.value)])
    if data.size > axis.size:
        data = data[:axis.size]
    if normalise.value :
        if dname == 'bm1_counts':
            tname = 'bm1_time'
        elif dname == 'bm2_counts':
            tname = 'bm2_time'
        else:
            tname = 'detector_time'
        norm = ds[tname]
        if norm != None and hasattr(norm, '__len__'):
            avg = norm.sum() / len(norm)
            niter = norm.item_iter()
            if niter.next() <= 0:
                niter.set_curr(1)
            data = data / norm * avg

    ds2 = Dataset(data, axes=[axis])
    ds2.title = ds.id
    ds2.location = fullname
    fit_min.value = axis.min()
    fit_max.value = axis.max()
    Plot1.set_dataset(ds2)
    Plot1.x_label = axis_name.value
    Plot1.y_label = str(data_name.value)
    Plot1.title = str(data_name.value) + ' vs ' + axis_name.value
    Plot1.pv.getPlot().setMarkerEnabled(True)

# This function is called when pushing the Run button in the control UI.
def __run_script__(fns):
    # Use the provided resources, please don't remove.
    global Plot1
    global Plot2
    global Plot3
    
    # check if a list of file names has been given
    if (fns is None or len(fns) == 0) :
        print 'no input datasets'
    else :
        for fn in fns:
            # load dataset with each file name
            ds = df[fn]
            print ds.shape
    print arg1_name.value
    
def __dispose__():
    global Plot1
    global Plot2
    global Plot3
    Plot1.clear()
    Plot2.clear()
    Plot3.clear()
