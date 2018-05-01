from gumpy.commons import sics
#from gumpy.quokka.quokka import *
from time import sleep

# Reldrive bsx
def reldriveBsx(offset):
    driveBsx(getBsxValue(), offset)

def scan_wavelength(wavelengthList, attList, mode, preset):
#    for wavelength in wavelengthList:
    for i in xrange(len(wavelengthList)):
        wavelength = wavelengthList[i]
        driveAtt(attList[i])
        sics.drive('nvs_lambda', wavelength)
        sleep(0.1)
#        for att in attListTrans:
#            driveAtt(att)
#            sleep(0.1)
        log('starting run, wavelength=')
        log(str(wavelength))
        quokka.scan(mode, dataType.HISTOGRAM_XY, preset)
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
wavelengthList = [5.76]
attList = [270]
###### USE THE FOLLOWING TWO LINES FOR MULTIPLE WAVELENGTHS ######
#wavelengthList = [4.502,5.0,5.76,6.0,7.0,8.0,10.0]
#attList[300,300,270,270,240,210,180]

if len(wavelengthList) != len(attList):
    raise Exception, 'number of wavelength must be the same as the number of att setup'
#scan mode
mode = scanMode.monitor
#how much counts you need
preset = 7.5E5

#pre-set, don't change
driveDet(19250, 0)
driveEntRotAp(180)

# configuration unpol 1
log('drive to configuration unpol 1')
driveGuide(guideConfig.g1)
#don't change below scan command
scan_wavelength(wavelengthList, attList, mode, preset)

# configuration -+
#polariser in
log('drive to configuration -+')
driveGuide(guideConfig.p1)
scan_wavelength(wavelengthList, attList, mode, preset)
#
# configuration --
#polariser in
log('drive to configuration --')
sics.set('/sample/isops/relay', 1)
sleep(1)
sics.set('/sample/isops/relay', 0)
scan_wavelength(wavelengthList, attList, mode, preset)
#
# configuration +-
# Drive flipper
log('drive to configuration +-')
driveFlipper(1)
#sics.set('/instrument/flipper/set_frequency', 407)
sleep(60)
scan_wavelength(wavelengthList, attList, mode, preset)

#
# configuration ++
# Drive flipper
log('drive to configuration ++')
sics.set('/sample/isops/relay', 1)
sleep(1)
sics.set('/sample/isops/relay', 0)
scan_wavelength(wavelengthList, attList, mode, preset)

# configuration unpol2
#polariser out
log('drive to configuration unpol 2')
driveFlipper(0)
sleep(3)
driveGuide(guideConfig.g1)
scan_wavelength(wavelengthList, attList, mode, preset)

######
log('experiment finished')