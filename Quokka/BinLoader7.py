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
        return 191 - self._helper.getCenterY()
    def getCenterY(self):
        return self._helper.getCenterX()
    def setCenter(self, centerX = -1, centerY = -1, minPixelCount = -1):
        if minPixelCount == -1:
            self._helper.setCenter(centerY, 191 - centerX)
        else:
            self._helper.setCenter(centerY, 191 - centerX, minPixelCount)
            
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

        # rotation -90deg (1.flip vertically 2.transpose)
        src = Array(self._helper.getHistogram())
        trp = array.instance(src.shape, dtype=int)
        Y   = src.shape[0]
        for y in xrange(Y):
            trp[Y - y - 1] = src[y]
        dst = Array(trp.__iArray__.getArrayUtils().transpose(0,1).getArray())

        self.Histogram = Dataset(dst)
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
            self._helper.loadTimeHistogram(centerY, 191 - centerX)
            #self._helper.loadTimeHistogram(centerX, centerY)

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
        
        if not filename.startswith('QKK') or not filename.endswith('.NX.HDF') or not number.isdigit():
            raise NameError('the specified nx-hdf filename does not match the pattern QKK#######.nx.hdf')
            
        number = int(number)
        if number > 99999:
            raise NameError('this version of the bin-loader only supports QKK files in the range of 0 to 99999')
        
        # set up double array for argument
        timestamps = jdoubles(len(self.Timestamps))
        for i in xrange(len(self.Timestamps)):
            timestamps[i] = self.Timestamps[i]
        
        # load selected time bins
        print 'loading time bins'
        timeBins = self._helper.loadTimeBins(timestamps)
        beamTime = self._helper.getBeamTime()
        print 'time bins loaded'
        
        ref = Dataset(self.NeXusPath)
        ref.__iDictionary__.addEntry('total_counts', '$entry/data/total_counts' )
        # monitor
        ref.__iDictionary__.addEntry('bm1_counts'  , '$entry/monitor/bm1_counts')
        ref.__iDictionary__.addEntry('bm1_time'    , '$entry/monitor/bm1_time'  )
        # beam time
        ref.__iDictionary__.addEntry('start_time'  , '$entry/instrument/detector/start_time')
        ref.__iDictionary__.addEntry('stop_time'   , '$entry/instrument/detector/stop_time')
        
        bm1_rate = ref.bm1_counts / ref.bm1_time
        time0    = ref.start_time
        if not isinstance(time0, float):
            if isinstance(time0, int):
                time0 = float(time0)
            else:
                time0 = time0[0]

        n = len(self.Timestamps)
        
        bt = -1 # beam time index
        tm = -1 # time bin index
        
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
            
            # rotation -90deg (1.flip vertically 2.transpose)
            src = Array(timeBins[tm])
            trp = array.instance(src.shape, dtype=int)
            Y   = src.shape[0]
            for y in xrange(Y):
                trp[Y - y - 1] = src[y]
            dst = Array(trp.__iArray__.getArrayUtils().transpose(0,1).getArray())

            ref.storage[0].copy_from(dst)
            ref.total_counts = dst.sum()
            ref.bm1_time     = (t1 - t0)
            ref.bm1_counts   = (t1 - t0) * bm1_rate # assuming that the rate is correct and constant for the current beam time
            ref.start_time   = int(time0 + t0)
            ref.stop_time    = int(time0 + t1)
            
            shortname = 'QKK%07i' % (number * 100 + tm)
            ref.__iNXroot__.getDefaultEntry().setShortName(shortname)
            ref.save_copy(path.join(directory, shortname + '.nx.hdf'))
            
            print shortname, 'created'
            
        print 'export completed'

    def invariantAnalysis(self, SDD, wavelength=5.0, resolution=200, exportPath=None, show=True):
        print 'invariant analysis'
        
        pixelW = 5.08
                
        centerX = self._helper.getCenterX()
        centerY = self._helper.getCenterY()
        binPath = self._helper.getBinPath()
        
        try:
            jLoader = BinLoadHelper()
            jLoader.loadFile(binPath, resolution)
            jLoader.loadTimeHistogram(centerX, centerY)
        
            data = Array(jLoader.getTimeHistogram())
            shape = data.shape
            
            T    = []
            dAdt = []
            Q2dQ = []
            var  = []
        
            q0 = 0
            for r in xrange(shape[0]):
                q1 = (2.0 * math.pi) / wavelength * math.atan(pixelW * r / SDD)
        
                Q2dQ.append(q1 * q1 * (q1 - q0))
                
                # for next iteration
                q0 = q1
               
            A1   = 0
            var1 = 0
            for t in xrange(shape[1]):
                
                A2   = 0.0
                var2 = 0.0
                for r in xrange(1, shape[0]):
                    # n = estimated number of pixels
                    #
                    # I_n = (I_1 + I_2 + ...) / n
                    #
                    # V_n = (I_1 + I_2 + ...) / n^2
                    #     = I_n / n
        
                    n = 2 * math.pi * (r - 0.5) 
                    
                    A2   += data[r, t] * Q2dQ[r]
                    var2 += data[r, t] * Q2dQ[r] * Q2dQ[r] / n
                    
                if t > 1:
                    T.append((t - 1) * resolution)
                    dAdt.append((A2 - A0) / (2 * resolution))
                    var.append((var2 + var0) / (4 * resolution * resolution))

                # for next iteration
                A0   = A1
                var0 = var1
                
                A1   = A2
                var1 = var2
                
            ds = Dataset(dAdt)
            
            ds.title = 'dA/dt'
                    
            axis0 = ds.axes[0]
            axis0.title = 'time'
            axis0.units = 'seconds'
            axis0.storage.copy_from(T)
            
            ds.var.storage.copy_from(var)
            #ds.var.storage.fill(0)
            
            if exportPath is not None:
                f = open(exportPath, 'w')
                for i in xrange(len(dAdt)):
                    f.write('%f, %e, %e\n' % (T[i], dAdt[i], math.sqrt(var[i])))
                f.close()

            if show:
                p = plot(ds)
                p.x_label ='time (seconds)'
                p.y_label =''
            
            print 'completed invariant analysis'
            return ds
        
        finally:
            del jLoader

#######################################################################
# start of program

'''
try:
    # release old data
    loader.close()
except:
    pass
'''

# load the bin file (filename, time bin with [seconds])

#loader = QuokkaBinLoader(r'C:/Gumtree/temp/bins/DAQ_2022-11-02T15-10-32/DATASET_0/EOS.bin', 10)
loader = QuokkaBinLoader(r'Z:\cycle\167\data\histserv\DAQ_2025-11-25T14-16-29\DATASET_0\EOS.bin', 10800)

# show content as normal 2d-histogram
loader.loadHistogram()
loader.showHistogram()

# show time histogram, which is dependent on the center position (radial averaging)! 
loader.setCenter(centerX = 92.6689, centerY = 97.2932) # center dose not affect resulting nexus-files, this is only for visualization within GumTree
loader.loadTimeHistogram()
loader.showTimeHistogram()

#loader.setManualTimeBins([0, 60])
loader.setEqualTimeBins(1200)                 # 600 seconds time bins

#bins = [0, 20]

#n = 20
#add = 0

#for i in xrange(n):
#    bins.append(bins[-1] + add)
    
#bins += [8000, 9000]
    
#print bins


#loader.setEqualTimeBins(10)
#loader.setManualTimeBins([58,60,62,64,66,68,70.5,72.5,74.5,76.5,78.5,80.5,83,85,87,89,91,93,95.5])
#loader.setGeometricTimeBins(10,0)
#loader.exportDatasets(r'U:\data\proposal\04676\EVENT_MODE_DATA\DAQ_2016-03-13T16-13-21\QKK0002277.nx.hdf')
#loader.exportDatasets(r'C:/Gumtree/temp/bins/QKK0032596.nx.hdf')
loader.exportDatasets(r'C:\Gumtree\temp\QKK0082608.nx.hdf')

print 'done'

# end of program
#######################################################################
