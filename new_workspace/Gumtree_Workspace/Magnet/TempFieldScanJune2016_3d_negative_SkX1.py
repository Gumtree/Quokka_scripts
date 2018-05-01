from gumpy.commons import sics
#from gumpy.quokka.quokka import *
from time import sleep

# Reldrive bsx
def reldriveBsx(offset):
    driveBsx(getBsxValue(), offset)


    
def scan_temp_field(fieldList, mode, preset, tempSettleTime = 1, fieldSettleTime = 1):
#    for wavelength in wavelengthList:
    for i in xrange(len(fieldList)):
        pack = fieldList[i]
#        driveAtt(attList[i])
#        log('driving tc1_driveable=' +  str(pack[0]))
        
        value = str(pack[0])
        
        log(value)
#        sics.drive('tc1_driveable', value)
#        log('waiting for temperature to settle')
#        sleep(tempSettleTime)
        fields = pack[1]
        for j in xrange(len(fields)):
            
            log('driving magnet1_driveable=' + str(0))
            sics.drive('ma1_setpoint', 0)
            sics.drive('tc1_driveable', 50)
            log('waiting for temperature to settle')
            log('driving magnet1_driveable=' + str(225))
            sics.drive('ma1_setpoint', 225)
            sics.drive('tc1_driveable', value)
            log(value)
            log('waiting for temperature to settle')
            sleep(900)
            field = fields[j][0]
            log('driving magnet1_driveable=' + str(field))
            sics.drive('ma1_setpoint', field)
            log('waiting for field to settle')
            sleep(fieldSettleTime)
            
            e_fields = fields[j][1]
            for k in xrange(len(e_fields)):
                e_field = e_fields[k]
                log('drive electronic field to ' + str(e_field))
#                sics.execute('setvolt ' + str(500))
#                sleep(15)
#                sics.execute('setvolt ' + str(1000))
#                sleep(15)
#                sics.execute('setvolt ' + str(1500))
#                sleep(10)
#                sics.execute('setvolt ' + str(2000))
#                sleep(10)
#                sics.execute('setvolt ' + str(2500))
#               sleep(1)
                sics.execute('setvolt ' + str(e_field))
                
#                prep_transmission()
#                quokka.scan(scanMode.time, dataType.HISTOGRAM_XY, 120)
#                
#                prep_scattering()
                log('start counting')
                quokka.scan(mode, dataType.HISTOGRAM_XY, preset)
#        for att in attListTrans:
#            driveAtt(att)
#            sleep(0.1)
#driveAtt(330)
# Set to long config
###### for ga ######

###polarisation out
def scan_temp_field_FW(fieldList, mode, preset, tempSettleTime = 1, fieldSettleTime = 1):
#    for wavelength in wavelengthList:
    sics.execute('setvolt ' + str(10))
    sleep(15)
    for i in xrange(len(fieldList)):
        pack = fieldList[i]
#        driveAtt(attList[i])
#        log('driving tc1_driveable=' +  str(pack[0]))
        
        value = str(pack[0])
        
        log(value)
#        sics.drive('tc1_driveable', value)
#        log('waiting for temperature to settle')
#        sleep(tempSettleTime)
        fields = pack[1]
        for j in xrange(len(fields)):
            
            log('driving magnet1_driveable=' + str(0))
            sics.drive('ma1_setpoint', 0)
            sics.drive('tc1_driveable', 50)
            log('waiting for temperature to settle')
            log('driving magnet1_driveable=' + str(225))
            sics.drive('ma1_setpoint', 225)
            sics.drive('tc1_driveable', value)
            log(value)
            log('waiting for temperature to settle')
            sleep(900)
            field = fields[j][0]
            log('driving magnet1_driveable=' + str(field))
            sics.drive('ma1_setpoint', field)
            log('waiting for field to settle')
            sleep(fieldSettleTime)
            
            e_fields = fields[j][1]
            for k in xrange(len(e_fields)):
                e_field = e_fields[k]
                log('drive electronic field to ' + str(e_field))
#                sics.execute('setvolt ' + str(500))
#                sleep(15)
#                sics.execute('setvolt ' + str(1000))
#                sleep(15)
#                sics.execute('setvolt ' + str(1500))
#                sleep(10)
#                sics.execute('setvolt ' + str(2000))
#                sleep(10)
#                sics.execute('setvolt ' + str(2500))
#               sleep(1)
                sics.execute('setvolt ' + str(e_field))
                
#                prep_transmission()
#                quokka.scan(scanMode.time, dataType.HISTOGRAM_XY, 120)
#                
#                prep_scattering()
                log('start counting')
                quokka.scan(mode, dataType.HISTOGRAM_XY, preset)

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
tempFieldList = [
                  (56.5,  #temperature 2
                    (
                     [225, [0,125,250,375,500,625,750,875,1000,]],
                    )
                  )
                 ]

tempSettleTime = 10
fieldSettleTime = 0
#attList = [270]
###### USE THE FOLLOWING TWO LINES FOR MULTIPLE WAVELENGTHS ######
#wavelengthList = [4.502,5.0,5.76,6.0,7.0,8.0,10.0]
#attList[300,300,270,270,240,210,180]

#if len(wavelengthList) != len(attList):
#    raise Exception, 'number of wavelength must be the same as the number of att setup'
#scan mode
#mode = scanMode.monitor
mode = scanMode.time
#how much counts you need
#preset = 7.0E6
preset = 300

#pre-set, don't change
#driveDet(19250, 0)
#driveEntRotAp(180)

# configuration unpol 1
# slog('drive to configuration 1')

#driveGuide(guideConfig.g1)
#don't change below scan command
log('experiment started')
scan_temp_field(tempFieldList, mode, preset, tempSettleTime, fieldSettleTime)

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