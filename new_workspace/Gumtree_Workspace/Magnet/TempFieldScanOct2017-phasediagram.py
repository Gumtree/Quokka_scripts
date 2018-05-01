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
                 #ZFC
                 (380,[10]),
                 (75, [10,1000,2000,3000,5000,8000,12000,10]),
                 (100, [1000,2000,3000,5000,8000,12000,10]),
                 (150, [1000,2000,3000,5000,8000,12000,10]),
                 (200, [1000,2000,3000,5000,8000,12000,10]),
                 (225, [1000,2000,3000,5000,8000,12000,10]),
                 (250, [1000,2000,3000,5000,8000,12000,10]),
                 (325, [1000,2000,3000,5000,8000,12000,10]),
                 (380, [1000]),
                 #FC first field
                 (75,[1000]),
                 (100,[1000]),
                 (150,[1000]),
                 (200,[1000]),
                 (225,[1000]),
                 (250,[1000]),
                 (325,[1000]),
                 #next field
                 (380,[2000]),
                 (75,[2000]),
                 (100,[2000]),
                 (150,[2000]),
                 (200,[2000]),
                 (225,[2000]),
                 (250,[2000]),
                 (325,[2000]),
                 #next field
                 (380,[3000]),
                 (75,[3000]),
                 (100,[3000]),
                 (150,[3000]),
                 (200,[3000]),
                 (225,[3000]),
                 (250,[3000]),
                 (325,[3000]),
                 #next field
                 (380,[5000]),
                 (75,[5000]),
                 (100,[5000]),
                 (150,[5000]),
                 (200,[5000]),
                 (225,[5000]),
                 (250,[5000]),
                 (325,[5000]),
                 #next field
                 (380,[8000]),
                 (75,[8000]),
                 (100,[8000]),
                 (150,[8000]),
                 (200,[8000]),
                 (225,[8000]),
                 (250,[8000]),
                 (325,[8000]),
                 #next field
                 (380,[12000]),
                 (75,[12000]),
                 (100,[12000]),
                 (150,[12000]),
                 (200,[12000]),
                 (225,[12000]),
                 (250,[12000]),
                 (325,[12000]),
                 #next field
                 (380,[0]),
                 #(56.75, [0,25,50,75,100,125,150,175,200,225,250,275,300,325,350,375,400]),
                 #(56.5, [0,25,50,75,100,125,150,175,200,225,250,275,300,325,350,375,400]),
                 #(56.25, [0,25,50,75,100,125,150,175,200,225,250,275,300,325,350,375,400]),
                 #(56, [0,25,50,75,100,125,150,175,200,225,250,275,300,325,350,375,400]),
                 #(55.75, [0,25,50,75,100,125,150,175,200,225,250,275,300,325,350,375,400]),
                 #(55.5, [0,25,50,75,100,125,150,175,200,225,250,275,300,325,350,375,400]),
                 #(55.25, [0,25,50,75,100,125,150,175,200,225,250,275,300,325,350,375,400]),
                 #(55, [0,25,50,75,100,125,150,175,200,225,250,275,300,325,350,375,400]),
                 #(54.75, [0,25,50,75,100,125,150,175,200,225,250,275,300,325,350,375,400]), 
                 #(54.5, [0,25,50,75,100,125,150,175,200,225,250,275,300,325,350,375,400]),
                 #(54.25, [0,25,50,75,100,125,150,175,200,225,250,275,300,325,350,375,400]),               
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