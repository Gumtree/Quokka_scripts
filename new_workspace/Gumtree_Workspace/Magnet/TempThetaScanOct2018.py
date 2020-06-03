from gumpy.commons import sics
from bragg.quokka.quokka import *
from time import sleep

# Reldrive bsx
def reldriveBsx(offset):
    driveBsx(getBsxValue(), offset)

def scan_temp_field(fieldList, mode, preset, tempSettleTime = 1, fieldSettleTime = 1):
#    for wavelength in wavelengthList:
    for i in xrange(len(fieldList)):
        pack = fieldList[i]
#        driveAtt(attList[i])
        log('driving tc1_driveable=' +  str(pack[0]))
        sics.drive('tc1_driveable', pack[0])
        log('waiting for temperature to settle')
        sleep(tempSettleTime)
        fields = pack[1]
        for j in xrange(len(fields)):
            field = fields[j]
            log('driving ma1_magnet_setpoint =' + str(field))
            sics.drive('ma1_magnet_setpoint', field)
            log('waiting for field to settle')
            sleep(fieldSettleTime)
            log('start counting')
            quokka.scan(mode, dataType.HISTOGRAM_XY, preset)

#        for att in attListTrans:
#            driveAtt(att)
#            sleep(0.1)
#driveAtt(330)
# Set to long config
###### for ga ######

###polarisation out

def scan_temp_theta(fieldList, mode, preset, tempSettleTime = 1, thetaSettleTime = 1):
#    for wavelength in wavelengthList:
    for i in xrange(len(fieldList)):
        pack = fieldList[i]
#        driveAtt(attList[i])
        log('driving tc1_driveable=' +  str(pack[0]))
        sics.drive('tc1_driveable', pack[0])
        log('waiting for temperature to settle')
        sleep(tempSettleTime)
        thetas = pack[1]
        for j in xrange(len(thetas)):
            theta = thetas[j]
            log('driving rotation=' + str(theta))
            sics.drive('samthet', theta)
            #slog('waiting for field to settle')
            sleep(thetaSettleTime)
            log('start counting')
            quokka.scan(mode, preset)

def scan_temp_field_theta(tempFieldList, thetaList, mode, preset, fieldSettleTime = 60, tempSettleTime = 1, thetaSettleTime = 1):
#    for wavelength in wavelengthList:
    for pack in tempFieldList:
#        driveAtt(attList[i])
        temp = pack[0]
        log('driving tc1_driveable=' +  str(temp))
        sics.drive('tc1_driveable', temp)
        log('waiting for temperature to settle')
        sleep(tempSettleTime)
        for field in pack[1]:
            log('driving ma1_magnet_setpoint =' + str(field))
            sics.drive('ma1_magnet_setpoint', field)
            log('waiting for field to settle')
            sleep(fieldSettleTime)

            for theta in thetaList :
                log('driving rotation=' + str(theta))
                sics.drive('samthet', theta)
                #slog('waiting for field to settle')
                sleep(thetaSettleTime)
                log('start counting')
                quokka.scan(mode, preset)

def scan_field_temp_theta(fieldTempList, mode, preset, fieldSettleTime = 60, tempSettleTime = 1):
#    for wavelength in wavelengthList:
    for pack in fieldTempList:
#        driveAtt(attList[i])
        field = pack[0]
        log('driving ma1_magnet_setpoint =' + str(field))
        sics.drive('ma1_magnet_setpoint', field)
        log('waiting for field to settle')
        sleep(fieldSettleTime)
        for temp in pack[1]:
            log('driving tc1_driveable=' +  str(temp))
            sics.drive('tc1_driveable', temp)
            log('waiting for temperature to settle')
            sleep(tempSettleTime)

            log('start counting')
            quokka.scan(mode, preset)

#            for theta in thetaList :
#                log('driving rotation=' + str(theta))
#                sics.drive('samthet', theta)
                #slog('waiting for field to settle')
#                sleep(thetaSettleTime)
#                log('start counting')
#                quokka.scan(mode, preset)

#wavelengthList = [8.00, 8.10, 8.20, 8.30, 8.40, 8.50, 8.60, 8.70, 8.80, 8.90, 9.00, 9.20, 9.40, 9.60]
#attListTrans = [150]

# Drive sample position
# Position 20 = MT beam; 12 = opal and 10 = T1
#setSample(20, 'empty beam')

# for transmission runs
#driveBsx(32.5,100)
#print 'Beam stop out...'

#the wavelength you want to scan on
#wavelengthList = [4.502, 5.0, 5.76, 6.0, 7.0, 8.0]

#thetaList = [-6, -3, 0, 3, 6]
thetaList = [0]

fieldTempList = [
                 #(5.31, [-0.3, 0, 0.3]),
#                  (320,[0]),
#                  (250,[0.0]),
#                  (320,[0.05]),
                  (0,[14,18,22,26,30,34,38,42,46,50,52,54,55,55.5,56,56.5,57,57.5,58,58.5,59,59.5,60]),
#                  (250,[0.05]),
#                  (280,[0.1]),
#                  (280,[0.2]),
#                  (280,[0.5]),
#                  (280,[1.0])
                 ]
      
tempSettleTime = 6
fieldSettleTime = 6
#thetaSettleTime = 5

#fieldList = [0, 0.005
#                ]
#attList = [270]
###### USE THE FOLLOWING TWO LINES FOR MULTIPLE WAVELENGTHS ######
#wavelengthList = [4.502,5.0,5.76,6.0,7.0,8.0,10.0]
#attList[300,300,270,270,240,210,180]

#if len(wavelengthList) != len(attList):
#    raise Exception, 'number of wavelength must be the same as the number of att setup'
#scan mode
#mode = scanMode.monitor
mode = ACQUISITION_MODE.time
#how much counts you need
#preset = 7.0E6
preset = 30

#pre-set, don't change
#driveDet(19250, 0)
#driveEntRotAp(180)

# configuration unpol 1
# slog('drive to configuration 1')

#driveGuide(guideConfig.g1)
#don't change below scan command
log('experiment started')

#scan_temp_field_theta(tempFieldList, thetaList, mode, preset, fieldSettleTime, tempSettleTime, thetaSettleTime)

scan_field_temp_theta(fieldTempList, mode, preset, fieldSettleTime, tempSettleTime)
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