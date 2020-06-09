import inspect
from java.lang import System
import time
import math
from gumpy.nexus.fitting import Fitting, GAUSSIAN_FITTING
from gumpy.commons.logger import n_logger
from gumpy.control import control
#from Internal import sicsext
from java.lang import Double
# Script control setup area
# script info
__script__.title = '2D Scan'
__script__.version = 'v0.1'
#pact = Act('previous_step()', '<- Previous Step')
    
G1 = Group('Dimension 1')
device1_name = Par('string', 'samx', options = ['samx'], command = 'update_axis1_name()')
device1_name.title = 'Device 1'
scan1_start = Par('float', 0)
scan1_start.title = 'Start'
scan1_stop = Par('float', 0)
scan1_stop.title = 'Stop'
scan1_np = Par('int', 0)
scan1_np.title = 'Number of points'
G1.add(device1_name, scan1_start, scan1_stop, scan1_np)

G2 = Group('Dimension 2')
device2_name = Par('string', 'samz', options = ['samz'], command = 'update_axis2_name()')
device2_name.title = 'Device 2'
scan2_start = Par('float', 0)
scan2_start.title = 'Start'
scan2_stop = Par('float', 0)
scan2_stop.title = 'Stop'
scan2_np = Par('int', 0)
scan2_np.title = 'Number of points'
G2.add(device2_name, scan2_start, scan2_stop, scan2_np)

scan_mode = Par('string', 'time', options = ['time', 'count'])
scan_mode.enabled = True
scan_mode.title = 'Scan mode'
scan_preset = Par('int', 0)
scan_preset.title = 'Scan preset'
act1 = Act('scan_device()', 'Scan on Devices')

def scan_device():
    np1 = int(scan1_np.value)
    if np1 <= 0:
        raise Exception, 'invalid number of points for dimension 1'
    np2 = int(scan2_np.value)
    if np2 <= 0:
        raise Exception, 'invalid number of points for dimension 2'
    
    motor1 = device1_name.value
    motor2 = device2_name.value
    
    start1 = scan1_start.value
    stop1 = scan1_stop.value
    start2 = scan2_start.value
    stop2 = scan2_stop.value
    
    if np1 == 1:
        step1 = 0.
    else:
        step1 = (stop1 - start1) * 1.0 / (np1 - 1)
        
    if np2 == 1:
        step2 = 0.
    else:
        step2 = (stop2 - start2) * 1.0 / (np2 - 1)
    
    mode = scan_mode.value
    preset = scan_preset.value

    slog('*********** scan started ***********')
    rev = False    
    for i in xrange(np1):
        pos1 = start1 + i * step1
        slog('drive ' + motor1  + ' ' + str(pos1))
        control.drive(motor1, pos1)
        for j in xrange(np2):
            if rev:
                pos2 = stop2 - j * step2
            else:
                pos2 = start2 + j * step2
            slog('drive ' + motor2  + ' ' + str(pos2))
            control.drive(motor2, pos2)
            
            slog('collect data with ' + motor1 + '=' + str(pos1) + ' and ' + 
                 motor2 + '=' + str(pos2) + ' on "' + mode + '" for preset of ' + 
                 str(preset))
            control.runscan('dummy_motor', 0, 0, 1, 
                            mode, preset)
        rev = not rev
    slog('*********** scan finished ***********')    
    
devices = control.get_drivables()
device1_name.options = devices
device2_name.options = devices
        


# This function is called when pushing the Run button in the control UI.
def __run_script__(fns):
#    __std_run_script__(fns)
    __std_run_script__(fns)

def load_experiment_data():
    basename = control.get_base_filename()
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


def __dataset_added__(fns = None):
    pass
    
def __std_run_script__(fns):
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
            ds = Plot1.ds
#            if ds != None and len(ds) > 0:
#                if ds[0].location == fn:
#                    return
            df.datasets.clear()
            ds = df[fn]
            axis_name.value = ds.axes[0].name
            dname = str(data_name.value)
            if dname == 'total_counts':
#                data = ds.sum(0)
                data = ds[dname]
            else:
                data = ds[dname]
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
        
            axis = ds.get_metadata(str(axis_name.value))
            if not hasattr(axis, '__len__'):
                axis = SimpleData([axis], title = (axis_name.value))
            ds2 = Dataset(data, axes=[axis])
            ds2.title = ds.id
            ds2.location = fn
            fit_min.value = axis.min()
            fit_max.value = axis.max()
            Plot1.set_dataset(ds2)
            Plot1.x_label = axis_name.value
            Plot1.y_label = dname
            Plot1.title = dname + ' vs ' + axis_name.value
            Plot1.pv.getPlot().setMarkerEnabled(True)
            peak_pos.value = float('NaN')
            FWHM.value = float('NaN')
            if auto_fit.value :
                fit_curve()
            
def auto_run():
    pass

def __dispose__():
    global Plot1
    global Plot2
    global Plot3
    Plot1.clear()
    Plot2.clear()
    Plot3.clear()
