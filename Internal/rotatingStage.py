# Script control setup area
# script info
__script__.title = 'Scan Device'
__script__.version = '0.1'

G1 = Group('Scan on device')
device_name = Par('string', 'dummy_motor', options = ['dummy_motor'], command = 'update_axis_name()')
scan_start = Par('float', 0)
scan_stop = Par('float', 0)
number_of_points = Par('int', 0)
scan_mode = Par('string', 'time', options = ['time', 'count'])
scan_mode.enabled = True
scan_preset = Par('int', 0)
act1 = Act('scan_device()', 'Scan on Device')
def scan_device():
    aname = str(device_name.value)
#    axis_name.value = aname
    np = int(number_of_points.value)
    if np <= 0:
        return
    step_size = float(scan_stop.value - scan_start.value) / np
    slog('runscan ' + str(device_name.value) + ' ' + str(scan_start.value) + ' ' + str(scan_stop.value) \
                    + ' ' + str(number_of_points.value) + ' ' + str(scan_mode.value) + ' ' + str(scan_preset.value))
    for p in xrange(np):
        slog('drive ' + aname + ' ' + str(scan_start.value + step_size * p))
        sics.drive(str(aname), scan_start.value + step_size * p)
        sicsext.runscan('dummy_motor', 0, 0, 1, 
                    scan_mode.value, scan_preset.value, None, True, \
                    'HISTOGRAM_XY')
        slog('finished NP ' + str(p))
        time.sleep(1)
    
devices = sicsext.getDrivables()
device_name.options = devices
def update_axis_name():
    axis_name.value = device_name.value
        
G1.add(device_name, scan_start, scan_stop, number_of_points, scan_mode, scan_preset, act1)


# Use below example to create a new Plot
# Plot4 = Plot(title = 'new plot')

# This function is called when pushing the Run button in the control UI.
def __run_script__(fns):
    global Plot1
    global Plot2
    global Plot3
    
    # check if a list of file names has been given
    if (fns is None or len(fns) == 0) :
        print 'no input datasets'
    else :
        for fn in fns:
            # load dataset with each file name
            ds = Plot3.ds
            if ds != None and len(ds) > 0:
                if ds[0].location == fn:
                    return
            df.datasets.clear()
            ds = df[fn]
            Plot3.set_dataset(ds[0])
    
def __dispose__():
    global Plot1
    global Plot2
    global Plot3
    Plot1.clear()
    Plot2.clear()
    Plot3.clear()
