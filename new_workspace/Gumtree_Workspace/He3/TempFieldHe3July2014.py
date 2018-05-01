from gumpy.commons import sics
#from gumpy.quokka.quokka import *
from time import sleep

# Reldrive bsx
def reldriveBsx(offset):
    driveBsx(getBsxValue(), offset)

#def setFlip(flag):
#    sics.set('/sample/isops/relay', flag)
#    if flag == 1:
#        sleep(60)
#    else:
#        sleep(1)

#cur_L2 = getDetPosition()
#if cur_L2 < 19000 or cur_L2 > 21000 :
#    slog('current L2 is not 20m, drive L2 to 20m')
#    driveConfig(20)

#def swopConfig():
#    global old_L2
#    if old_L2 == 20:
#        driveConfig(4)
#        old_L2 = 4
#    elif old_L2 == 4:
#        driveConfig(20)
#        old_L2 = 20
#old_L2 = 20
#slog('Please make sure your current guide configuration is for L2=20')

#
#        for att in attListTrans:
#            driveAtt(att)
#            sleep(0.1)
#driveAtt(330)
# Set to long config
###### for ga ######

###polarisation out


#wavelengthList = [8.00, 8.10, 8.20, 8.30, 8.40, 8.50, 8.60, 8.70, 8.80, 8.90, 9.00, 9.20, 9.40, 9.60]
#attListTrans = [150]

# Drive sample position
# Position 20 = MT beam; 12 = opal and 10 = T1
#setSample(20, 'empty beam')

# for transmission runs
#driveBsx(32.5,100)
#print 'Beam stop out...'


def setFlip(flag):
    sics.set('/sample/isops/relay', 1)
    sleep(60)
    sics.set('/sample/isops/relay', 0)
    sleep(60)
   
def driveConfig(L2,bsx,bsz):
    slog('start driving detector...')
    slog('L2=' + str(L2) + ' bsx=' + str(bsx) + ' bsz=' + str(bsz) + ' att=330')
    driveAtt(330)    
    sics.run('bsx', bsx)
    sics.run('bsz', bsz)
    driveDet(L2, 0)
    sics.drive('bsx', bsx)
    sics.drive('bsz', bsz)
    slog('drive completed')

def run_transmission_scan(mode, preset):
    slog('drive beam stop out, att=330')
    driveAtt(330)
    sics.run('bsz', 10)
    slog('drive polariser in')
    driveGuide(guideConfig.p1)
    sics.drive('bsz', 10)
    driveAtt(60)
#
    slog('trans ++ att=60 det=20m count=' + str(preset))
    setFlip(1)
    slog('counting...')
    quokka.scan(mode, dataType.HISTOGRAM_XY, preset)
#
    slog('trans +- att=60 det=20m count=' + str(preset))
    setFlip(0)
    slog('counting...')
    quokka.scan(mode, dataType.HISTOGRAM_XY, preset)
#
    slog('tran unpolarised att=75 det=20m count=' + str(preset))
    driveAtt(330)
    slog('polariser out')
    driveGuide(guideConfig.ga)
    driveAtt(75)
    slog('counting...')
    quokka.scan(mode, dataType.HISTOGRAM_XY, preset)
#Drive beam stop back in
    slog('drive beam stop back in, att=330')
    driveAtt(330)
    sics.drive('bsz', 245)


def run_scattering_scan(mode, presetSpinPlus, presetSpinMinus, bsx, bsz, att):
    slog('drive polariser in, att=330')
    driveAtt(330)
    sics.run('bsx', bsx)
    sics.run('bsz', bsz)
    driveGuide(guideConfig.p1)
    sics.drive('bsx', bsx)
    sics.drive('bsz', bsz)
   
    driveAtt(att)
#
    slog('spin=++ att=' + str(att) +' count=' + str(presetSpinPlus))
    setFlip(1)
    slog('counting...')
    quokka.scan(mode, dataType.HISTOGRAM_XY, presetSpinPlus)
#
    slog('spin=+- att=' + str(att) +' count=' + str(presetSpinMinus))
    setFlip(0)
    slog('counting...')
    quokka.scan(mode, dataType.HISTOGRAM_XY, presetSpinMinus)


def setTemperature(setpoint, heaterRange, waitForTemperature, tempSettleTime): 
    slog('set tc1 heater range=' + str(heaterRange))
    sics.set('/sample/tc1/heater/heaterRange',heaterRange)
    if waitForTemperature==0:
        slog('set sample T=' +  str(setpoint) + ' & not wait for it')
        sics.run('tc1_driveable', setpoint)
    else:
        slog('set sample T=' +  str(setpoint) + ' & wait till it is reached')
        sics.drive('tc1_driveable', setpoint)
        sleep(tempSettleTime)
        slog('waiting '+ str(tempSettleTime) +'sec for temperature to settle')
        

def scan_temp_conf(L2List, bsxList, bszList, polAttList, tempList, heaterRangeList, mode, presetList, tempSettleTime = 1, fieldSettleTime = 1):
#    for wavelength in wavelengthList:
    for i in xrange(len(tempList)):
#begin setting temperature and proceed to driving the detector
        setTemperature(tempList[i],heaterRangeList[i],0,tempSettleTime)
#Drive detector to L2=20m
        driveConfig(L2List[0],bsxList[0],bszList[0])
#set and this time wait till 
        if tempList[i] <> 4.2:
            setTemperature(tempList[i],heaterRangeList[i],1,tempSettleTime)
#
        run_scattering_scan(mode, presetList[1], presetList[2], bsxList[0], bszList[0], polAttList[0])
        run_transmission_scan(mode, presetList[0])
#L2=4m
        driveConfig(L2List[1],bsxList[1],bszList[1])
        run_scattering_scan(mode, presetList[3], presetList[4], bsxList[1], bszList[1], polAttList[1])


#main
tempSettleTime=600
fieldSettleTime=0

L2List = [19250,3200]
bsxList=[30,32.5]
bszList=[245,260]
polAttList=[35,0]

tempList = [
                 150,
                 80,
                 200,
                 ]
#heater range: 0=off, 1=2.5mW, 2=25mW, 3=250mW, 4=2.5W, 5=25W
heaterRangeList = [
                 5,
                 4,
                 5,
                   ]

tempSettleTime = 600

#scan mode
mode = scanMode.monitor
#mode = scanMode.time
#how much counts you need
#preset = 7.0E6
presetList = [
              3336000,
              6950000,
              54400000,
              28350000,
             111200000,
            ]

#pre-set, don't change
#driveDet(19250, 0)
#driveEntRotAp(180)

# configuration unpol 1
# slog('drive to configuration 1')

#driveGuide(guideConfig.g1)
#don't change below scan command
slog('experiment started')
scan_temp_conf(L2List, bsxList, bszList, polAttList, tempList, heaterRangeList, mode, presetList, tempSettleTime, fieldSettleTime)
#slog('heat the sample up to 300K')
#setTemperature(300,5,0)
# configuration -+
#polariser in
#log('drive to configuration 2')
#driveGuide(guideConfig.p1)
#scan_temp_field(tempFieldList, mode, preset, tempSettleTime, fieldSettleTime)
#
# configuration --
#polariser in
#log('drive to configuration --')
#sics.set('/sample/isops/relay', 1)
#sleep(1)
#sics.set('/sample/isops/relay', 0)
#scan_wavelength(wavelengthList, attList, mode, preset)
##
## configuration +-
## Drive flipper
#log('drive to configuration +-')
#driveFlipper(1)
##sics.set('/instrument/flipper/set_frequency', 407)
#sleep(60)
#scan_wavelength(wavelengthList, attList, mode, preset)
#
##
## configuration ++
## Drive flipper
#log('drive to configuration ++')
#sics.set('/sample/isops/relay', 1)
#sleep(1)
#sics.set('/sample/isops/relay', 0)
#scan_wavelength(wavelengthList, attList, mode, preset)
#
## configuration unpol2
##polariser out
#log('drive to configuration unpol 2')
#driveFlipper(0)
#sleep(3)
#driveGuide(guideConfig.g1)
#scan_wavelength(wavelengthList, attList, mode, preset)

######
log('experiment finished')