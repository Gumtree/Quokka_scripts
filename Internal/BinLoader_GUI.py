'''
@author:        davidm
@organization:  ANSTO

@version:  1.7.0.1
@date:     11/04/2012
@source:   http://www.nbi.ansto.gov.au/quokka/scripts/

'''

# Script control setup area
# script info
__script__.title = 'Event File Loader'
__script__.version = ''

from org.gumtree.data.nexus.utils import BinLoadHelper

from gumpy.nexus import *
from gumpy.vis.plot1d import *
from gumpy.vis.image2d import *
from gumpy.vis.event import *
from gumpy.commons.jutils import jdoubles

from os import path
from math import pi, atan

_event_dirty_flag = False

class QuokkaBinLoader:

    Histogram         = None
    HistogramPlot     = None
    TimeHistogram     = None
    TimeHistogramPlot = None
    Masks             = None
    Timestamps        = None
    HDF_REF           = None

    # reference file
    NeXusPath = None

    def __init__(self, path = None, histo_bins_t = -1, hdf_path = None):
        self._helper = BinLoadHelper()
        
        # initialize mouse click
        self._mouseListener = MouseListener()
        self._mouseListener.on_click = self.onMouseClick
        
        if path is None or len(path.strip()) == 0:
            raise Exception('please provide a valid event file path')
        
        if hdf_path is None or len(hdf_path.strip()) == 0:
            raise Exception('please provide a valid HDF file path')
        
        # load file
        self.loadHDF(hdf_path)
        self.loadFile(path, histo_bins_t)
            
    def close(self):
        if not self.Histogram is None:
            self.Histogram.close()
            self.Histogram = None
            
        if not self.TimeHistogram is None:
            self.TimeHistogram.close()
            self.TimeHistogram = None
            
        self.Masks      = []
        self.Timestamps = []
        self._helper = None
        self._mouseListener = None

    def getTimeBinLength(self):
        return self._helper.getTimeBinLength()
    def getBinPath(self):
        return self._helper.getBinPath()
    def getNxPath(self):
        return self.NeXusPath
    def getCenterX(self):
        return self._helper.getCenterX()
    def getCenterY(self):
        return self._helper.getCenterY()
    def setCenter(self, centerX = -1, centerY = -1, minPixelCount = -1):
        if minPixelCount == -1:
            self._helper.setCenter(centerX, centerY)
        else:
            self._helper.setCenter(centerX, centerY, minPixelCount)
            
    def setNeXusFile(self, path):
        self.NeXusPath = path;
            
    # event handling    
    def onMouseClick(self, e):
        print 'clicked on (' + str(int(e.getX())) + ', ' + str(int(e.getY())) + ')'
    
    # functions
    def loadFile(self, path, histo_bins_t = -1):
        print 'loading bin file'
        self._helper.loadFile(path, histo_bins_t)
        print 'bin file loaded'

    def loadHistogram(self, startTime = 0, endTime = -1):
        print 'loading histogram'
        self._helper.loadHistogram(startTime, endTime)

        self.Histogram = Dataset(Array(self._helper.getHistogram()))
        self.Histogram.title = 'Histogram'
                
        axis0 = self.Histogram.axes[0]
        axis0.title = 'y'
        axis0.units = 'pixels'
        
        axis1 = self.Histogram.axes[1]
        axis1.title = 'x'
        axis1.units = 'pixels'

        print 'histogram loaded'
    def loadTimeHistogram(self, centerX = -1, centerY = -1):
        print 'loading time histogram'
        if (centerX == -1) and (centerY == -1):
            self._helper.loadTimeHistogram()
        else:
            self._helper.loadTimeHistogram(centerX, centerY)

        self.TimeHistogram = Dataset(Array(self._helper.getTimeHistogram()))
        self.TimeHistogram.title = 'Time-Histogram'
        
        axis0 = self.TimeHistogram.axes[0]
        axis0.title = 'radius'
        axis0.units = 'pixels'
    
        axis1 = self.TimeHistogram.axes[1]
        axis1.title = 'time'
        axis1.units = 'seconds'
        # adjust axes
        axis1.copy_from(axis1 * self._helper.getTimeBinLength())
        
        print 'time histogram loaded'
    def showHistogram(self):
        if self.Histogram is None:
            self.loadHistogram()
#        if (self.HistogramPlot is None) or self.HistogramPlot.pv.isDisposed():
#            self.HistogramPlot = image(self.Histogram)
#            self.HistogramPlot.add_mouse_listener(self._mouseListener)
#        else:
#            self.HistogramPlot.set_dataset(self.Histogram)
        Plot1.set_dataset(self.Histogram)
        if (self.HistogramPlot is None) or self.HistogramPlot.pv.isDisposed():
            self.HistogramPlot = Plot1
            self.HistogramPlot.add_mouse_listener(self._mouseListener)
    def showTimeHistogram(self):
        if self.TimeHistogram is None:
            self.loadTimeHistogram()
#        if (self.TimeHistogramPlot is None) or self.TimeHistogramPlot.pv.isDisposed():
#            self.TimeHistogramPlot = image(self.TimeHistogram)
#        else:
#            self.TimeHistogramPlot.set_dataset(self.TimeHistogram)
        Plot2.set_dataset(self.TimeHistogram)
        if (self.TimeHistogramPlot is None) or self.TimeHistogramPlot.pv.isDisposed():
            self.TimeHistogramPlot = Plot2
    def exportTimeHistogram(self, folder, file_q, file_t, file_i, upsideDown=False):
        # fetch information
        ds     = self.TimeHistogram
        axis_r = ds.axes[0]
        axis_t = ds.axes[1]
        axis_q = Array(axis_r)
        
        axis_rLen = len(axis_r)
        
        # conversion radius to q
        factor = 2 * pi / 5.0;
        for index_r in xrange(axis_rLen):    
            alpha = atan(axis_r[index_r] * 0.00508 / 4.07163)    
            axis_q[index_r] = factor * alpha    
            #print "%15.6g" % axis_q[index_r]
            
        # write q (1d)
        f = None
        try:
            f = open(folder + file_q, 'w')
            
            itr_q = axis_q
            if upsideDown:
                itr_q = reversed(itr_q)
                
            for q in itr_q:
                f.write(str(q) + '\n')
        finally:
            if f is not None:
                f.close()
        print file_q, 'saved'
           
        # write time (1d)
        f = None
        try:
            f = open(folder + file_t, 'w')
            for t in axis_t:
                f.write(str(t) + '\n')
        finally:
            if f is not None:
                f.close()
        print file_t, 'saved'
        
        # write intensity map (2d)
        f = None
        try:
            f = open(folder + file_i, 'w')
            
            itr_r = xrange(axis_rLen)
            if upsideDown:
                itr_r = reversed(itr_r)
                
            for index_r in itr_r:
                for index_t in xrange(len(axis_t)):
                    f.write(str(ds[index_r, index_t]) + ',')
                f.write('\n')
        finally:
            if f is not None:
                f.close()
        print file_i, 'saved'
        
        # successful completion
        print 'done'

    def removeMasks(self):
        if (not self.Masks is None) and (not self.TimeHistogramPlot is None) and not self.TimeHistogramPlot.pv.isDisposed():
            for mask in self.Masks:
                self.TimeHistogramPlot.remove_mask(mask)
                
        self.Timestamps = []
        self.Masks      = []
    def setManualTimeBins(self, timestamps):
        self.showTimeHistogram()
        self.removeMasks()

        rCount = self.TimeHistogram.storage.shape[0] # self._maxRIndex 
        tCount = self.TimeHistogram.storage.shape[1]

        is_inclusive = True
        offsetY = 0.5
        y_min   = -offsetY
        y_max   = -offsetY + rCount

        index = 0

        t0 = 0
        tN = tCount * self._helper.getTimeBinLength()
        for timestamp in timestamps:
            if timestamp < t0:
                raise AttributeError('timestamps')
            if timestamp == t0:
                continue
        
            t1 = timestamp
            if t1 >= tN:
                break
            
            self.Timestamps.append(t0)
            self.Masks.append(self.TimeHistogramPlot.add_mask_2d(t0, t1, y_min, y_max, str(index), is_inclusive))
            index += 1
            # shift time span
            t0 = t1
            # swap color
            is_inclusive = not is_inclusive
        # final mask
        self.Timestamps.append(t0)
        self.Masks.append(self.TimeHistogramPlot.add_mask_2d(t0, tN, y_min, y_max, str(index), is_inclusive))
    def setEqualTimeBins(self, timespan):
        if timespan <= 0:
            raise AttributeError('timespan')
        self.showTimeHistogram()
        self.removeMasks()

        rCount = self.TimeHistogram.storage.shape[0]
        tCount = self.TimeHistogram.storage.shape[1]
        
        is_inclusive = True
        offsetY = 0.5
        y_min   = -offsetY
        y_max   = -offsetY + rCount

        index = 0
        
        t0 = 0
        t1 = timespan
        tN = tCount * self._helper.getTimeBinLength()
        while t1 < tN:
            self.Timestamps.append(t0)
            self.Masks.append(self.TimeHistogramPlot.add_mask_2d(t0, t1, y_min, y_max, str(index), is_inclusive))
            index += 1
            # shift time span
            t0  = t1
            t1 += timespan
            # swap color
            is_inclusive = not is_inclusive
            
        # final mask
        self.Timestamps.append(t0)
        self.Masks.append(self.TimeHistogramPlot.add_mask_2d(t0, tN, y_min, y_max, str(index), is_inclusive))
    def setGeometricTimeBins(self, firstTimespan, startTime = 0, mirrored = False):
        if firstTimespan <= 0:
            raise AttributeError('firstTimespan')
        if startTime < 0:
            raise AttributeError('startTime')
        self.showTimeHistogram()
        self.removeMasks()

        rCount = self.TimeHistogram.storage.shape[0]
        tCount = self.TimeHistogram.storage.shape[1]
        
        is_inclusive = True
        offsetY = 0.5
        y_min   = -offsetY
        y_max   = -offsetY + rCount
        
        index = 0
        
        if startTime != 0:
            if not mirrored:
                self.Timestamps.append(0)
                self.Masks.append(self.TimeHistogramPlot.add_mask_2d(0, startTime, y_min, y_max, str(index), is_inclusive))
                index += 1
                # swap color
                is_inclusive = not is_inclusive
            else:
                ts = firstTimespan
                t0 = startTime - ts
                t1 = startTime
                while t0 > 0:
                    self.Timestamps.append(t0)
                    self.Masks.append(self.TimeHistogramPlot.add_mask_2d(t0, t1, y_min, y_max, None, is_inclusive))
                    # double time span
                    ts *= 2
                    # shift time span
                    t1  = t0
                    t0 -= ts
                    # swap color
                    is_inclusive = not is_inclusive
                # final mask
                self.Timestamps.append(0)
                self.Masks.append(self.TimeHistogramPlot.add_mask_2d(0, t1, y_min, y_max, None, is_inclusive))
                # set correct names
                self.Timestamps.reverse()
                self.Masks.reverse()
                for mask in self.Masks:
                    mask.setName(str(index))
                    index += 1
                is_inclusive = False
                
        ts = firstTimespan
        t0 = startTime
        t1 = startTime + ts
        tN = tCount * self._helper.getTimeBinLength()
        while t1 < tN:
            self.Timestamps.append(t0)
            self.Masks.append(self.TimeHistogramPlot.add_mask_2d(t0, t1, y_min, y_max, str(index), is_inclusive))
            index += 1
            # double time span
            ts *= 2
            # shift time span
            t0  = t1
            t1 += ts
            # swap color
            is_inclusive = not is_inclusive
        # final mask
        self.Timestamps.append(t0)
        self.Masks.append(self.TimeHistogramPlot.add_mask_2d(t0, tN, y_min, y_max, str(index), is_inclusive))

    def loadHDF(self, hdf_path):
        self.NeXusPath = hdf_path
        self.directory = path.dirname(self.NeXusPath)
        self.filename  = path.basename(self.NeXusPath).upper()
        self.HDF_REF = Dataset(self.NeXusPath)
        self.HDF_REF.__iDictionary__.addEntry('data_counts', '$entry/data/total_counts' )
        self.HDF_REF.__iDictionary__.addEntry('total_counts', '$entry/instrument/detector/total_counts' )
        # monitor
        self.HDF_REF.__iDictionary__.addEntry('bm1_counts'  , '$entry/monitor/bm1_counts')
        self.HDF_REF.__iDictionary__.addEntry('bm1_time'    , '$entry/monitor/bm1_time'  )
        # beam time
        self.HDF_REF.__iDictionary__.addEntry('start_time'  , '$entry/instrument/detector/start_time')
        self.HDF_REF.__iDictionary__.addEntry('stop_time'   , '$entry/instrument/detector/stop_time')
        # frame size
#        self.HDF_REF.__iDictionary__.addEntry('frame_size'   , '$entry/instrument/detector/time_of_flight')
#        self.HDF_REF.__iDictionary__.addEntry('detector_time', '$entry/instrument/detector/time' )
#        self.HDF_REF.__iDictionary__.addEntry('bsx'   , '$entry/instrument/parameters/BeamCenterX')
#        self.HDF_REF.__iDictionary__.addEntry('bsz'   , '$entry/instrument/parameters/BeamCenterZ')        
        BinLoadHelper.FILE_FRAME_LENGTH = int(self.HDF_REF.time_of_flight.max())
#        BinLoadHelper.FILE_FRAME_LENGTH = 20000

    def getFileNumber(self):
        fn = self.filename
        if len(fn) == 17 and fn.startswith('QKK') and fn.endswith('.NX.HDF'):
            number    = int(fn[3:10])
        else:
            fn = str(self.HDF_REF.file_name.storage.__iArray__.toString())
            number = fn[-14:-7]
        if number > 99999:
            number = number % 100000
        return number
        
    def exportDatasets(self, exportPath = None):
        if (self.Timestamps is None) or (self.Timestamps.count == 0):
            raise NameError('no time bins were specified')
        
        # check file name convention
        if not exportPath is None and len(exportPath) > 0:
            self.directory = exportPath
#        number    = self.filename[3:self.filename.find('.NX.HDF')]
        
        
#        if not self.filename.startswith('QKK') or not self.filename.endswith('.NX.HDF') or not number.isdigit():
#            raise NameError('the specified nx-hdf filename does not match the pattern QKK#######.nx.hdf')
#            
#        number = int(number)
#        if number > 99999:
#            raise NameError('this version of the bin-loader only supports QKK files in the range of 0 to 99999')
        number = self.getFileNumber()
        
        log("file number set to be: {}".format(number))
        
        # set up double array for argument
        timestamps = jdoubles(len(self.Timestamps))
        for i in xrange(len(self.Timestamps)):
            timestamps[i] = self.Timestamps[i]
        
        log("timestamp sequence: {}".format(timestamps))
        
        # load selected time bins
        log('loading time bins')
        timeBins = self._helper.loadTimeBins(timestamps)
        beamTime = self._helper.getBeamTime()
        log('time bins loaded')
        log('beam time from event binary file: {}'.format(beamTime))
        
        bm1_rate = self.HDF_REF.bm1_counts / self.HDF_REF.bm1_time
        if (type(self.HDF_REF.start_time) == int):
            time0 = self.HDF_REF.start_time
        else:
            time0 = self.HDF_REF.start_time[0]
        
        n = len(self.Timestamps)
        
        bt = -1 # beam time index
        tm = -1 # time bin index
        
        log('start time stamp from the HDF file: {}'.format(time0))
        
        t1 = 0
        while t1 < beamTime:
            t0 = t1
            bt += 1
            if bt < n:
                t1 = self.Timestamps[bt]
            else:
                t1 = beamTime
            
            if t1 <= 0:
                continue
            tm += 1
            if t1 <= t0:
                continue
            
            timeBin = Array(timeBins[tm])
            self.HDF_REF.storage.copy_from(timeBin)          # <---- ref.storage[0].copy_from(timeBin)
            s = timeBin.sum()
            self.HDF_REF.total_counts = s
            self.HDF_REF.data_counts = s
            self.HDF_REF.bm1_time     = (t1 - t0)
            self.HDF_REF.bm1_counts   = (t1 - t0) * bm1_rate # assuming that the rate is correct and constant for the current beam time
            self.HDF_REF.start_time   = int(time0 + t0)
            self.HDF_REF.stop_time    = int(time0 + t1)
            
            shortname = 'QKK%07i' % (number * 100 + tm)
            self.HDF_REF.__iNXroot__.getDefaultEntry().setShortName(shortname)
            fn = path.join(self.directory, shortname + '.nx.hdf')
            self.HDF_REF.save_copy(fn)
            
            log('{} created'.format(fn))
            
        log('export completed')

#######################################################################
# start of program


#try:
#    # release old data
#    loader.close()
#except:
#    pass

# load the bin file

###EPG INSERTS HERE###
#loader = QuokkaBinLoader(r'Z:\cycle\current\data\histserv\DAQ_2025-02-19T17-33-43\DATASET_0\EOS.bin', 30)
#loader = QuokkaBinLoader(r'W:\hsdata\DAQ_2013-12-20T01-07-24\DATASET_0\EOS.bin', 30)

'''
loader = QuokkaBinLoader(r'D:\temp\quokka\DAQ_2025-11-23T21-48-18\DATASET_0\EOS.bin', -1)

# show content as normal 2d-histogram
loader.loadHistogram()
loader.showHistogram()

# show time histogram, which is dependent on the center position (radial averaging)! 
loader.setCenter(centerX = 94, centerY = 94) # center dose not affect resulting nexus-files, this is only for visualization within GumTree
loader.loadTimeHistogram()
loader.showTimeHistogram()

# specify time bins 
###EPG ADDED SECTIONS HERE###
#loader.setEqualTimeBins(7200)                 # 600 seconds time bins

loader.setEqualTimeBins(2400)                 # 600 seconds time bins

###EPG ADDED SECTIONS HERE###
#loader.setManualTimeBins([500, 3000, 5000]) # new bin at 500, 3000 and 5000 seconds
#loader.setManualTimeBins([8300, 11000, 15400, 18200])
#loader.setManualTimeBins([972, 1392, 1632, 1992, 2172, 2532, 2712, 3672, 3852, 5172, 5472, 5652, 5832, 6132])
loader.setManualTimeBins([1279, 1339, 1543, 1603, 1778, 1838, 1898, 1958, 2140, 2200, 2345, 2405, 2421, 2481, 2662, 2722, 2919, 3850, 4156, 5399, 5459, 5635, 5695, 5775, 5835, 5974, 6034, 6333, 8232])

# export time bins to nexus files
###EPG ADDED SECTIONS HERE###
#loader.exportDatasets('C:/Documents and Settings/davidm/Desktop/DAQ_2011-10-13T15-03-13/QKK0033259.nx.hdf') # this will create QKK3151000.nx.hdf - QKK3151009.nx.hdfloader.exportDatasets('C:/Documents and Settings/davidm/Desktop/DAQ_2011-10-13T15-03-13/QKK0033259.nx.hdf') # this will create QKK3151000.nx.hdf - QKK3151009.nx.hdf
loader.exportDatasets(r'D:\Data\DSC data temp\DSC streamed temp\DAQ_2013-10-04T11-31-52_Test10\QKK0051098.nx.hdf')

#loader.exportTimeHistogram(r'D:\Data\DSC data temp\DSC streamed temp\DAQ_2013-10-04T11-31-52_Test10/', "q0.csv", "t0.csv", "i0.csv", upsideDown=False)
###EPG ADDED SECTIONS HERE###
#loader.setManualTimeBins([500, 3000])
###EPG ADDED SECTIONS HERE###
#loader.exportDatasets(r'D:\Users\quokka\Desktop\David\New folder\QKK0054620.nx.hdf')
#loader.exportDatasets(r'W:\data\proposal\00105\2025\2025_02_19_EPG_EVENT_MODE_TESTING\QKK0069403.nx.hdf')
loader.exportDatasets(r'D:\temp\quokka\res\QKK0082596.nx.hdf')

'''

gl = Group('Read from event and HDF files')
event_file = Par('file', '', command = 'set_dirty_flag()')
event_file.title = 'Event file'
event_file.ext = '*.bin'

HDF_file = Par('file', '', command = 'set_dirty_flag()')
HDF_file.title = 'HDF file'
HDF_file.ext = '*.hdf'

centre_x = Par('float', 94, command = 'set_dirty_flag()')
centre_x.title = 'Centre X'
centre_y = Par('float', 94, command = 'set_dirty_flag()')
centre_y.title = 'Centre Z'

load_act = Act('load_files()', 'Load files')
gl.add(event_file, HDF_file, centre_x, centre_y, load_act)

gp = Group('Parameters from HDF file')
gp.numColumns = 2
frame_size = Par('int', 0)
frame_size.title = 'ToF frame size (us)'
frame_size.colspan = 2

beam_time = Par('int', 0)
beam_time.title = 'Beam time (s)'
beam_time.colspan = 2

bsx = Par('float', 0)
bsx.title = 'BeamCenterX'
bsx.colspan = 2

bsz = Par('float', 0)
bsz.title = 'BeamCenterZ'
bsz.colspan = 2

total_counts = Par('int', 0)
total_counts.title = 'Detector total counts'
total_counts.colspan = 2

space_1 = Par('space')
apply_act = Act('apply_beamcentres()', 'Apply beam centre and re-plot')

gp.add(frame_size, beam_time, total_counts, bsx, bsz, space_1, apply_act)

go = Group('Re-segment and export')
go.numColumns = 20

_EXPORT_FOLDER_INTRO = '[same as HDF path]'
export_folder = Par('file', _EXPORT_FOLDER_INTRO)
export_folder.title = 'to Folder'
export_folder.dtype = 'folder'
export_folder.colspan = 20

equal_flag = Par('bool', True, command = 'change_equal_flag()')
equal_flag.title = 'Equal time bin'
equal_flag.colspan = 13

equal_size = Par('int', 60)
equal_size.title = 'size (s)'
equal_size.colspan = 7

manual_flag = Par('bool', False, command = 'change_manual_flag()')
manual_flag.title = 'Manual time bin'
manual_flag.colspan = 13

_MANUAL_SIZE_INTRO = "array, comma as delimiter"
manual_size = Par('str', _MANUAL_SIZE_INTRO, 
                  command = 'manual_size_blured()')
manual_size.title = 'timestamps (s)'
manual_size.enabled = False
manual_size.focus = 'manual_size_focused()'
manual_size.colspan = 7

export_act = Act('export_files()', 'Export')
export_act.colspan = 20

go.add(export_folder, equal_flag, equal_size, 
       manual_flag, manual_size, export_act)

def apply_beamcentres():
    centre_x.value = bsx.value
    centre_y.value = bsz.value
    load_files()
    
def set_dirty_flag():
    global _event_dirty_flag
    log('event file dirty')
    _event_dirty_flag = True
    
def manual_size_focused():
    if manual_size.value == _MANUAL_SIZE_INTRO:
        manual_size.value = ''
        
def manual_size_blured():
    if len(manual_size.value.strip()) == 0:
        manual_size.value = _MANUAL_SIZE_INTRO
    else:
        par = manual_size.value.strip()
        if len(par) == 0:
            logErr('empty size')
            return
        if ',' in par:
            if not par.startswith('['):
                par = '[' + par + ']'
        try:
            val = eval(par)
        except:
            logErr('invalid target values: ' + par)
            return
    
def change_equal_flag():
    enabled = equal_flag.value
    equal_size.enabled = enabled
    manual_flag.value = not enabled
    manual_size.enabled = not enabled

def change_manual_flag():
    enabled = manual_flag.value
    equal_size.enabled = not enabled
    equal_flag.value = not enabled
    manual_size.enabled = enabled
    
_quokka_loader = None
def load_files():
    global _quokka_loader, _event_dirty_flag
    if _quokka_loader != None:
        try:
            _quokka_loader.close()
        except:
            logErr('failed to close existing loader')
    _quokka_loader = QuokkaBinLoader(str(event_file.value), -1,
                                     str(HDF_file.value))
    # show content as normal 2d-histogram
    _quokka_loader.loadHistogram()
    _quokka_loader.showHistogram()
    
    # show time histogram, which is dependent on the center position (radial averaging)! 
    _quokka_loader.setCenter(centre_x.value, centre_y.value) # center dose not affect resulting nexus-files, this is only for visualization within GumTree
    _quokka_loader.loadTimeHistogram(centre_x.value, centre_y.value)
    _quokka_loader.showTimeHistogram()
    
    hdf = _quokka_loader.HDF_REF
    frame_size.value = int(hdf.time_of_flight.max())
    beam_time.value = int(hdf.detector_time)
    total_counts.value = hdf.total_counts
    bsx.value = hdf.BSXmm
    bsz.value = hdf.BSZmm
    
    _event_dirty_flag = False

def export_files():
    global _quokka_loader, _event_dirty_flag
    if _quokka_loader is None or _event_dirty_flag:
        load_files()
    if equal_flag.value:
        _quokka_loader.setEqualTimeBins(equal_size.value)
    elif manual_flag.value:
        par = manual_size.value.strip()
        if len(par) == 0:
            logErr('empty manual time bin size')
            return
        if ',' in par:
            if not par.startswith('['):
                par = '[' + par + ']'
        try:
            val = eval(par)
        except:
            logErr('invalid target values: ' + par)
            return
        log('set manual time bins: {}'.format(val))
        _quokka_loader.setManualTimeBins(val)
        
    directory = str(export_folder.value)
    if len(directory.strip()) == 0 or directory==_EXPORT_FOLDER_INTRO:
        log('export to the same folder as the HDF file')
        directory = None
    _quokka_loader.exportDatasets(directory)
    log('done')
    
print 'Initiated'

def __dispose__():
    global Plot1
    global Plot2
    global Plot3
    Plot1.clear()
    Plot2.clear()
    Plot3.clear()
    global _quokka_loader
    if not _quokka_loader is None:
        _quokka_loader.close()
        _quokka_loader = None

#event_file.value = r'D:\temp\quokka\DAQ_2025-11-23T21-48-18\DATASET_0\EOS.bin'
#HDF_file.value = r'D:\temp\quokka\QKK0282596.nx.hdf'
#export_folder.value = r'D:\temp\quokka\r1'
#equal_size.value = 3600
# end of program
#######################################################################
