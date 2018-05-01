from gumpy.commons import sics
#from gumpy.quokka.quokka import *
from time import sleep

# Reldrive bsx
def reldriveBsx(offset):
    driveBsx(getBsxValue(), offset)
    
def prep_transmission():
    sics.drive('att', 210)
    reldriveBsx(100)
#    driveBsx(36, 100)
    
def prep_scattering():
    reldriveBsx(-100)
#    driveBsx(36, -100)
    sics.drive('att', 0)

def scan_temp_field(fieldList, mode, preset, tempSettleTime = 1, fieldSettleTime = 1):
#    for wavelength in wavelengthList:
    for i in xrange(len(fieldList)):
        pack = fieldList[i]
#        driveAtt(attList[i])

        log('driving magnet1_driveable=' + str(0))
#HERE        sics.drive('ma1_setpoint', 0)

        log('driving tc1_driveable=' +  str(pack[0]))  
        value = str(pack[0])
        log(value)
        sics.drive('tc1_driveable', value)
        log('waiting for temperature to settle')
        sleep(tempSettleTime)
        fields = pack[1]
        for j in xrange(len(fields)):
#            log('driving magnet1_driveable=' + str(0))
#            sics.drive('ma1_setpoint', 0)
#            sics.drive('tc1_driveable', 80)
#            log('waiting for temperature to settle')
#            sleep(10)
#            sics.drive('tc1_driveable', value)
#            log('waiting for temperature to settle')
#            sleep(900)
            field = fields[j]
            log('driving magnet1_driveable=' + str(field))
            sics.drive('ma1_setpoint', field)
            log('waiting for field to settle')
            sleep(fieldSettleTime)
            log('start counting')
#            prep_transmission()
#            quokka.scan(scanMode.time, 'HISTOGRAM_XY', 60)
#            prep_scattering()
            quokka.scan(mode, preset)
            log('file saved at ' + str(sics.get_base_filename()))
  
#            prep_transmission()
#            quokka.scan('time', 'HISTOGRAM_XY', 60)
#            prep_scattering()
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

#the wavelength you want to scan on
#wavelengthList = [4.502, 5.0, 5.76, 6.0, 7.0, 8.0]
tempFieldList = [
                 (100, [1000,2000,3000,5000,8000,12000,10]),
                 ]

tempSettleTime = 60
fieldSettleTime = 0
#attList = [270]
###### USE THE FOLLOWING TWO LINES FOR MULTIPLE WAVELENGTHS ######
#wavelengthList = [4.502,5.0,5.76,6.0,7.0,8.0,10.0]
#attList[300,300,270,270,240,210,180]

#if len(wavelengthList) != len(attList):
#    raise Exception, 'number of wavelength must be the same as the number of att setup'
#scan mode
#mode = scanMode.monitor
#mode = scanMode.time
mode = 'time'
#how much counts you need
#preset = 7.0E6
preset = 1200

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