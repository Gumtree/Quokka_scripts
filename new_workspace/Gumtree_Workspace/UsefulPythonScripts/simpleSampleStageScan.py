# Script control setup area
# script info
__script__.title = 'Multiple Sample Scan'
__script__.version = '1.0'

_collection_list = [
                    [2, 'dDhA kinetic', 0],
                    [3, 'hDdA kinetic', 0],
                    ]

# Use below example to create parameters.
# The type can be string, int, float, bool, file.
loop_size = Par('int', 2)
count_mode = Par('string', 'time', options=['time', 'count'])
count_preset = Par('float', 5)


# Use below example to create a button
act1 = Act('act1_changed()', 'run scan') 
def act1_changed():
#    sn = guide_names.value
    for i in range(loop_size.value):
        slog('now in loop ' + str(i))
        if len(_collection_list) > 0:
            if count_mode.value == 'time':
                mode = scanMode.time
            else:
                mode = scanMode.count
            for item in _collection_list:
                slog('L' + str(i) + ': drive to sample ' + str(item[0]))
                driveSample(item[0])
                sics.execute('samplename {' + str(item[1]) + '}')
                if (item[2] > 0) :
                    preset = item[2]
                else:
                    preset = count_preset.value
                slog('L' + str(i) + ': scan ' + str(mode) + ' ' + str(preset))
                quokka.scan(mode, dataType.HISTOGRAM_XY, preset)
                slog('L' + str(i) + ': file saved at ' + sics.get_base_filename())
    slog('done')
    
# Use below example to create a new Plot
# Plot4 = Plot(title = 'new plot')

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
