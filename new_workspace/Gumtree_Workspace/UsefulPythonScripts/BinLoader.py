'''
@author:        davidm
@organization:  ANSTO

@version:  1.7.0.1
@date:     11/04/2012
@source:   http://www.nbi.ansto.gov.au/quokka/scripts/

'''

from org.gumtree.data.nexus.utils import BinLoadHelper

from gumpy.nexus import *
from gumpy.vis.plot1d import *
from gumpy.vis.image2d import *
from gumpy.vis.event import *
from gumpy.commons.jutils import jdoubles

from os import path
from math import pi, atan

class QuokkaBinLoader:

    Histogram         = None
    HistogramPlot     = None
    TimeHistogram     = None
    TimeHistogramPlot = None
    Masks             = None
    Timestamps        = None

    # reference file
    NeXusPath = None

    def __init__(self, path = None, histo_bins_t = -1):
        self._helper = BinLoadHelper()
        
        # initialize mouse click
        self._mouseListener = MouseListener()
        self._mouseListener.on_click = self.onMouseClick
        
        # load file
        if not path is None:
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
        if (self.HistogramPlot is None) or self.HistogramPlot.pv.isDisposed():
            self.HistogramPlot = image(self.Histogram)
            self.HistogramPlot.add_mouse_listener(self._mouseListener)
        else:
            self.HistogramPlot.set_dataset(self.Histogram)
    def showTimeHistogram(self):
        if self.TimeHistogram is None:
            self.loadTimeHistogram()
        if (self.TimeHistogramPlot is None) or self.TimeHistogramPlot.pv.isDisposed():
            self.TimeHistogramPlot = image(self.TimeHistogram)
        else:
            self.TimeHistogramPlot.set_dataset(self.TimeHistogram)
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

        rCount = loader.TimeHistogram.storage.shape[0] # self._maxRIndex 
        tCount = loader.TimeHistogram.storage.shape[1]

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
            self.Masks.append(self.TimeHistogramPlot.add_mask(t0, t1, y_min, y_max, str(index), is_inclusive))
            index += 1
            # shift time span
            t0 = t1
            # swap color
            is_inclusive = not is_inclusive
        # final mask
        self.Timestamps.append(t0)
        self.Masks.append(self.TimeHistogramPlot.add_mask(t0, tN, y_min, y_max, str(index), is_inclusive))
    def setEqualTimeBins(self, timespan):
        if timespan <= 0:
            raise AttributeError('timespan')
        self.showTimeHistogram()
        self.removeMasks()

        rCount = loader.TimeHistogram.storage.shape[0]
        tCount = loader.TimeHistogram.storage.shape[1]
        
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
            self.Masks.append(self.TimeHistogramPlot.add_mask(t0, t1, y_min, y_max, str(index), is_inclusive))
            index += 1
            # shift time span
            t0  = t1
            t1 += timespan
            # swap color
            is_inclusive = not is_inclusive
            
        # final mask
        self.Timestamps.append(t0)
        self.Masks.append(self.TimeHistogramPlot.add_mask(t0, tN, y_min, y_max, str(index), is_inclusive))
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
                self.Masks.append(self.TimeHistogramPlot.add_mask(0, startTime, y_min, y_max, str(index), is_inclusive))
                index += 1
                # swap color
                is_inclusive = not is_inclusive
            else:
                ts = firstTimespan
                t0 = startTime - ts
                t1 = startTime
                while t0 > 0:
                    self.Timestamps.append(t0)
                    self.Masks.append(self.TimeHistogramPlot.add_mask(t0, t1, y_min, y_max, None, is_inclusive))
                    # double time span
                    ts *= 2
                    # shift time span
                    t1  = t0
                    t0 -= ts
                    # swap color
                    is_inclusive = not is_inclusive
                # final mask
                self.Timestamps.append(0)
                self.Masks.append(self.TimeHistogramPlot.add_mask(0, t1, y_min, y_max, None, is_inclusive))
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
            self.Masks.append(self.TimeHistogramPlot.add_mask(t0, t1, y_min, y_max, str(index), is_inclusive))
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
        self.Masks.append(self.TimeHistogramPlot.add_mask(t0, tN, y_min, y_max, str(index), is_inclusive))

    def exportDatasets(self, nexusReference = None):
        print '0'
        
        if not nexusReference is None:
            self.NeXusPath = nexusReference
        if self.NeXusPath is None:
            raise NameError('no reference nexus file was specified')
        if (self.Timestamps is None) or (self.Timestamps.count == 0):
            raise NameError('no time bins were specified')
        
        # check file name convention
        directory = path.dirname(self.NeXusPath)
        filename  = path.basename(self.NeXusPath).upper()
        number    = filename[3:filename.find('.NX.HDF')]
        
        print 'a'
        
        if not filename.startswith('QKK') or not filename.endswith('.NX.HDF') or not number.isdigit():
            raise NameError('the specified nx-hdf filename does not match the pattern QKK#######.nx.hdf')
            
        number = int(number)
        if number > 99999:
            raise NameError('this version of the bin-loader only supports QKK files in the range of 0 to 99999')
        
        print 'b'
        
        # set up double array for argument
        timestamps = jdoubles(len(self.Timestamps))
        for i in xrange(len(self.Timestamps)):
            timestamps[i] = self.Timestamps[i]
        
        print 'c'
        
        # load selected time bins
        print 'loading time bins'
        timeBins = self._helper.loadTimeBins(timestamps)
        beamTime = self._helper.getBeamTime()
        print 'time bins loaded'
        
        print 'd'
        
        ref = Dataset(self.NeXusPath)
        ref.__iDictionary__.addEntry('total_counts', '$entry/data/total_counts' )
        # monitor
        ref.__iDictionary__.addEntry('bm1_counts'  , '$entry/monitor/bm1_counts')
        ref.__iDictionary__.addEntry('bm1_time'    , '$entry/monitor/bm1_time'  )
        # beam time
        ref.__iDictionary__.addEntry('start_time'  , '$entry/instrument/detector/start_time')
        ref.__iDictionary__.addEntry('stop_time'   , '$entry/instrument/detector/stop_time')
        
        print 'e'
        
        bm1_rate = ref.bm1_counts / ref.bm1_time
        time0    = ref.start_time[0]
        
        n = len(self.Timestamps)
        
        bt = -1 # beam time index
        tm = -1 # time bin index
        
        print 'f'
        
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
            ref.storage.copy_from(timeBin)          # <---- ref.storage[0].copy_from(timeBin)
            ref.total_counts = timeBin.sum()
            ref.bm1_time     = (t1 - t0)
            ref.bm1_counts   = (t1 - t0) * bm1_rate # assuming that the rate is correct and constant for the current beam time
            ref.start_time   = int(time0 + t0)
            ref.stop_time    = int(time0 + t1)
            
            shortname = 'QKK%07i' % (number * 100 + tm)
            ref.__iNXroot__.getDefaultEntry().setShortName(shortname)
            ref.save_copy(path.join(directory, shortname + '.nx.hdf'))
            
            print shortname, 'created'
            
        print 'export completed'

#######################################################################
# start of program


try:
    # release old data
    loader.close()
except:
    pass

# claim HMS time of flight frame size
BinLoadHelper.FILE_FRAME_LENGTH = 40000

# load the bin file
loader = QuokkaBinLoader(r'D:\Data\DSC data temp\DSC streamed temp\DAQ_2013-10-04T11-31-52_Test10\DATASET_0\EOS.bin', 30)

# show content as normal 2d-histogram
loader.loadHistogram()
loader.showHistogram()

# show time histogram, which is dependent on the center position (radial averaging)! 
loader.setCenter(centerX = 97.328, centerY = 96.374) # center dose not affect resulting nexus-files, this is only for visualization within GumTree
loader.loadTimeHistogram()
loader.showTimeHistogram()

# specify time bins 
#loader.setEqualTimeBins(7200)                 # 600 seconds time bins
#loader.setManualTimeBins([500, 3000, 5000]) # new bin at 500, 3000 and 5000 seconds
#loader.setManualTimeBins([8300, 11000, 15400, 18200])
#loader.setManualTimeBins([972, 1392, 1632, 1992, 2172, 2532, 2712, 3672, 3852, 5172, 5472, 5652, 5832, 6132])
loader.setManualTimeBins([1279, 1339, 1543, 1603, 1778, 1838, 1898, 1958, 2140, 2200, 2345, 2405, 2421, 2481, 2662, 2722, 2919, 3850, 4156, 5399, 5459, 5635, 5695, 5775, 5835, 5974, 6034, 6333, 8232])

# export time bins to nexus files
#loader.exportDatasets('C:/Documents and Settings/davidm/Desktop/DAQ_2011-10-13T15-03-13/QKK0033259.nx.hdf') # this will create QKK3151000.nx.hdf - QKK3151009.nx.hdf
#loader.exportDatasets(r'D:\Data\DSC data temp\DSC streamed temp\DAQ_2013-10-04T11-31-52_Test10\QKK0051098.nx.hdf')

loader.exportTimeHistogram(r'D:\Data\DSC data temp\DSC streamed temp\DAQ_2013-10-04T11-31-52_Test10/', "q0.csv", "t0.csv", "i0.csv", upsideDown=False)

print 'done'

# end of program
#######################################################################
