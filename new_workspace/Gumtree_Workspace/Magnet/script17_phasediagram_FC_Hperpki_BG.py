from gumpy.commons import sics
#from gumpy.quokka.quokka import *
from time import sleep


######################
# GLOBAL settings
mode = "time" # can be changed to mode = scanMode.monitor
tempSettleTime = 45 # time for settling at each temperature step
fieldSettleTime = 0 # time for settling at each field step
highTemp = 4 # for FC before changing field heat to this temperature, also for ZFC before new temperature
lowTemp = 1.6 # for FW before changing field cool to this temperature
highTempSettleTime = 30 # time for settling at max high temperature
lowTempSettleTime = 60 # time for settling at minimum low temperature
firstTempSettleTime = 30 # time for settling at first measurement point after changing temperature
firstFieldSettleTime = 0 # time for settling at first measurement point after changing field
thetaSettleTime = 5 # time for settling after changing theta
measurementTime = 60 # time for each measurement

  
def scan_temp_field_FC(measurementList, mode, preset, tempSettleTime = 1, fieldSettleTime = 1):
    for field,tempList in measurementList:
        log('driving magnet1_driveable=' + str(0))
        sics.drive('ma1_magnet_setpoint', 0) 
        log('waiting for field to settle')
        sleep(fieldSettleTime)
        log('driving tc1_driveable=' +  str(highTemp))
        sics.drive('tc1_driveable', highTemp)
        log('waiting for temperature to settle')
        sleep(highTempSettleTime)        
        log('driving magnet1_driveable=' + str(field))
        sics.drive('ma1_magnet_setpoint', field)
        log('waiting for field to settle')
        sleep(fieldSettleTime)
        
        for i,temp in enumerate(tempList):
            log('driving tc1_driveable=' + str(temp))
            sics.drive('tc1_driveable', temp)         
            log('waiting for temperature to settle')
            if i ==0:
                sleep(firstTempSettleTime)
            else:
                sleep(tempSettleTime)
            
            for theta in [-6,-4,-2.,0.,2.,4.,6.]:
                log('driving rotation=' + str(theta))
                sics.drive('samthet', theta)
                sleep(thetaSettleTime)
                log('start counting')
                quokka.scan(mode, preset)

    log('driving magnet1_driveable=' + str(0))
    sics.drive('ma1_magnet_setpoint', 0)
    
def scan_theta(thetaList, mode, preset):
    for theta in thetaList:
        log('driving rotation=' + str(theta))
        sics.drive('samthet', theta)
        sleep(thetaSettleTime)
        log('start counting')
        quokka.scan(mode, preset)
                     
            
# list for measurements using the FC protocol
listFC_temp = [3.2,3.0,2.8,2.6,2.4,2.2,2.0,1.8,1.6]
listFC = [
            (0.000, listFC_temp),            
            (0.100, listFC_temp),            
            (0.200, listFC_temp),            
            (0.300, listFC_temp),
            (0.050, listFC_temp),
            (0.150, listFC_temp),
            (0.250, listFC_temp),
            (0.350, listFC_temp),
            (0.400, listFC_temp)
        ]


wideThetaList = [-8.,-6.,-4.,-2.,0.,2.,4.,6.,8.,10.]
tightThetaList = [-6.,-4.,-2.,0.,2.,4.,6.]
### from here actual scans are defined
#log('experiment started')

scan_theta(wideThetaList, mode, 60)
scan_theta(tightThetaList, mode, 240)
scan_temp_field_FC(listFC, mode, measurementTime, tempSettleTime, fieldSettleTime)
#scan_temp_field_ZFC(listZFC, mode, measurementTime, tempSettleTime, fieldSettleTime)
#scan_temp_field_FW(listFW, mode, measurementTime, tempSettleTime, fieldSettleTime)
#scan_temp_helical_FW(listHelicalFW_temp, mode, measurementTime, tempSettleTime, fieldSettleTime)
#scan_singlefield_FC(listFC_temp, mode, measurementTime, tempSettleTime, fieldSettleTime)

######
#log('experiment finished')
