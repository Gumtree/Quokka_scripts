# Script control setup area
# script info
__script__.title = 'Repair Broken File'
__script__.version = ''
from java.io import File

# Use below example to create parameters.
# The type can be string, int, float, bool, file.


# Use below example to create a button
act1 = Act('repair()', 'Click to Repair Selected Files') 
def repair():
    dss = __DATASOURCE__.getSelectedDatasets()
    if dss is None or len(dss) <= 1:
        print 'Please select more than one files to combine.'
        return
    path = selectSaveFolder()
    if path == None:
        return
    fi = File(path)
    if not fi.exists():
        if not fi.mkdir():
            print 'Error: failed to make directory: ' + path
            return
    
    hds = None
    
    for dinfo in dss:
        loc = dinfo.getLocation()
        ds = df[str(loc)]
        if hds is None:
            hds = ds
        else:
            hds += ds
            hds.total_counts += ds.total_counts
            hds.detector_time += ds.detector_time
            hds.bm1_counts += ds.bm1_counts
            hds.bm1_time += ds.bm1_time
            if ds.bm1_time > 0:
                hds.bm1_event_rate += hds.bm1_counts / hds.bm1_time - hds.bm1_event_rate
            hds.bm2_counts += ds.bm2_counts
            hds.bm2_time += ds.bm2_time
            if ds.bm2_time > 0:
                hds.bm2_event_rate += hds.bm2_counts / hds.bm2_time - hds.bm2_event_rate
            hds.bm3_counts += ds.bm3_counts
            hds.bm3_time += ds.bm3_time
            if ds.bm3_time > 0:
                hds.bm3_event_rate += hds.bm3_counts / hds.bm3_time - hds.bm3_event_rate
    savepath = path + '/' + ('QKK%07d' % hds.id) + '.nx.hdf'
    hds.save_copy(str(savepath))
    print 'Fixed file saved to ' + savepath
            
                
            

def harvest_metadata(ds):
    meta = dict()
    if hasattr(ds, '__iDictionary__') :
        keys = ds.__iDictionary__.getAllKeys().toArray()
        for key in keys :
            item = ds.__iNXroot__.findDataItem(key.getName())
            if item:
                meta[key.getName()] = SimpleData(item)
        items = ds.__iNXroot__.getDataItemList()
        for item in items :
            name = str(item.getShortName())
            meta[name] = SimpleData(item)
    return meta
# Use below example to create a new Plot
# Plot4 = Plot(title = 'new plot')

# This function is called when pushing the Run button in the control UI.
def __run_script__(fns):
    pass
    
def __dispose__():
    global Plot1
    global Plot2
    global Plot3
    Plot1.clear()
    Plot2.clear()
    Plot3.clear()
