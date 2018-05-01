from gumpy.commons import sics
#from gumpy.quokka.quokka import *
from time import sleep

# Reldrive bsx
def reldriveBsx(offset):
    driveBsx(getBsxValue(), offset)

#driveAtt(330)

# Set to long config
driveEntRotAp(0)
driveGuide(guideConfig.lens)
driveDet(19250, 300)

######

wavelengthList = [7.0, 7.25, 7.50, 7.70, 7.80, 7.90, 8.00, 8.07, 8.20, 8.30, 8.40, 8.50, 8.60, 8.70, 8.80, 8.90, 9.00]
#wavelengthList = [8.00, 8.10, 8.20, 8.30, 8.40, 8.50, 8.60, 8.70, 8.80, 8.90, 9.00, 9.20, 9.40, 9.60]
attListTrans = [150]

# Drive sample position
# Position 20 = MT beam; 12 = opal and 10 = T1
setSample(20, 'empty beam')

# for transmission runs
driveBsx(32.5,100)
print 'Beam stop out...'
print 'starting run, wavelength='
print wavelength

for wavelength in wavelengthList:
    sics.drive('nvs_lambda', wavelength)
    sleep(0.1)
    for att in attListTrans:
        driveAtt(att)
        sleep(0.1)
        quokka.scan(scanMode.monitor, dataType.HISTOGRAM_XY, 5E6)
        sleep(0.1)

driveAtt(330)    