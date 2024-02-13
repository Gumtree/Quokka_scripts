# Script control setup area
# script info
__script__.title = 'Search for invalid value'
__script__.version = '1.0'

from org.gumtree.data.impl.netcdf import NcDataItem 
# Use below example to create parameters.
# The type can be string, int, float, bool, file.

arg_path = Par('str', '/sample/diameter')
arg_path.title = 'Path of variable'

arg_value = Par('float', 99999.0)
arg_value.title = 'Invalid Value'

arg_new = Par('float', float('nan'))
arg_new.title = 'New value'

act2 = Act('search_files()', 'Search')
def search_files():
    inv_value = arg_value.value
    if math.isnan(inv_value) :
        print 'can not search for NaN value'
        return
#    new_val = arg_value.value
#    if math.isnan(new_val):
#        print 'can not replace to NaN value'
#        return
    
    for n in __selected_dataset__:
        df.datasets.clear()
        ds = df[str(n)]
        p = '$entry' + arg_path.value
        node = ds[str(p)]
        if node == inv_value:
            print 'found ' + n
    print 'done'
    

# Use below example to create a button
act1 = Act('patch_value()', 'Patch') 
def patch_value():
    folder = selectSaveFolder()
    if folder == None:
        return
    inv_value = arg_value.value
    if math.isnan(inv_value) :
        print 'can not search for NaN value'
        return
    new_value = arg_new.value
    if math.isnan(new_value):
        print 'can not replace to NaN value'
        return
    
    for n in __selected_dataset__:
        df.datasets.clear()
        ds = df[str(n)]
        p = '$entry' + arg_path.value
        node_value = ds[str(p)]
        if node_value == inv_value:
            print "patching " + n
            node = ds.get_metadata(str(p))
            node[0] = new_value
            new_path = folder + '/' + ds.name
            ds.save_copy(new_path)
    print 'done'
    
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
