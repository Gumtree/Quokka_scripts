# Script control setup area
# script info
__script__.title = 'Patch value in HDF files'
__script__.version = '1.0'

from org.gumtree.data.impl.netcdf import NcDataItem 
# Use below example to create parameters.
# The type can be string, int, float, bool, file.

arg_path = Par('str', '/sample/name')
arg_path.title = 'Path of variable'

arg_value = Par('str', '')
arg_value.title = 'New value'

# Use below example to create a button
act1 = Act('patch_value()', 'Patch') 
def patch_value():
    folder = selectSaveFolder()
    if folder == None:
        return
    new_val = arg_value.value
    val_array = array.Array(new_val, [len(new_val)], str).__iArray__
    
    for n in __selected_dataset__:
        df.datasets.clear()
        ds = df[str(n)]
        print "patching " + n
        p = '$entry' + arg_path.value
        root = ds.__iNXroot__
        item = root.findContainerByPath(p)
        pare = item.getParentGroup()
        new_item = NcDataItem(pare, item.getShortName(), val_array)
        pare.addDataItem(new_item)
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
