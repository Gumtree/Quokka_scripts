# Script control setup area
# script info
__script__.title = 'Search for invalid value'
__script__.version = '1.0'

from org.gumtree.data.impl.netcdf import NcDataItem 
# Use below example to create parameters.
# The type can be string, int, float, bool, file.

diameter_path = '$entry/sample/diameter'
apx_name = 'apx'

act2 = Act('search_files()', 'Search')
def search_files():
    inv_value = 99999.0
    if math.isnan(inv_value) :
        print 'can not search for NaN value'
        return
#    new_val = arg_value.value
#    if math.isnan(new_val):
#        print 'can not replace to NaN value'
#        return
    count = 0
    oc = 0
    for n in __selected_dataset__:
        df.datasets.clear()
        ds = df[str(n)]
        node = ds[str(diameter_path)]
        if node == inv_value:
            print n
            count += 1
        oc += 1
    print 'found {} ones with invalid diameter value out of {} files.'.format(count, oc)
    

# Use below example to create a button
act1 = Act('patch_value()', 'Patch') 
def patch_value():
    folder = selectSaveFolder()
    if folder == None:
        return
    inv_value = 99999.0
    ct = 0
    for n in __selected_dataset__:
        df.datasets.clear()
        ds = df[str(n)]
        node_value = ds[str(diameter_path)]
        if node_value == inv_value:
            node = ds.get_metadata(str(diameter_path))
            apx_value = ds.apx
            if abs(apx_value + 47) < 1:
                new_value = 7.5
            elif abs(apx_value + 98) < 1:
                new_value = 12.5
            else:
                print 'invalid apx value: {}'.format(apx_value)
                continue
            print "patching {} with new value {}".format(n, new_value)
            node[0] = new_value
            new_path = folder + '/' + ds.name
            ds.save_copy(new_path)
            ct += 1
    print 'done, patched {} files.'.format(ct)
    
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
