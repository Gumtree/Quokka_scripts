'''
@author:        davidm
@organization:  ANSTO

@version:  1.9.0.1
@date:     28/11/2013
@source:   http://www.nbi.ansto.gov.au/quokka/scripts/

'''

from gumpy.nexus import *
import os.path as path

def QkkSplit(nexusPath):
    # check file name convention
    directory = path.dirname(nexusPath)
    filename  = path.basename(nexusPath).upper()
    number    = filename[3:filename.find('.NX.HDF')]
    
    if not filename.startswith('QKK') or not filename.endswith('.NX.HDF') or not number.isdigit():
        raise NameError('the specified nx-hdf filename does not match the pattern QKK#######.nx.hdf')
        
    number = int(number)
    if number > 99999:
        raise NameError('this version of the bin-loader only supports QKK files in the range of 0 to 99999')
    
    ref = Dataset(nexusPath)
    ref.__iDictionary__.addEntry('total_counts', '$entry/data/total_counts'  )
    ref.__iDictionary__.addEntry('time_stamps' , '$entry/data/time_of_flight')
    ## monitor
    ref.__iDictionary__.addEntry('bm1_counts'  , '$entry/monitor/bm1_counts')
    #ref.__iDictionary__.addEntry('bm1_time'    , '$entry/monitor/bm1_time'  )
    # beam time
    #ref.__iDictionary__.addEntry('start_time'  , '$entry/instrument/detector/start_time')
    #ref.__iDictionary__.addEntry('stop_time'   , '$entry/instrument/detector/stop_time')
            
    shape = ref.shape
    src   = ref.storage
    dst   = zeros([1, 1, shape[2], shape[3]]).storage
    
    ref.storage = dst
    
    total_time = ref.time_stamps.max()
    bm1_rate   = ref.bm1_counts / total_time # ref.bm1_time

    for i in xrange(shape[1]):
        dst[0, 0].copy_from(src[0, i])
        
        this_time = ref.time_stamps[i + 1] - ref.time_stamps[i]
        
        ref.bm1_counts   = bm1_rate * this_time
        ref.total_counts = int(dst[0, 0].sum())
    
        shortname = 'QKK%07i' % (number * 100 + i + 1)

        ref.__iNXroot__.getDefaultEntry().setShortName(shortname)
        
        print 'saving...'
        ref.save_copy(path.join(directory, shortname + '.nx.hdf'))            
        print shortname, 'created'
        
    print 'export completed'

#######################################################################
# start of program

QkkSplit(r'W:\data\proposal\02434\some_real_runs\QKK0053940.nx.hdf')

print 'done'

# end of program
#######################################################################
