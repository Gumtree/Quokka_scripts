from gumpy.commons import sics
#from gumpy.quokka.quokka import *
from time import sleep


######################
# GLOBAL settings
mode = "time" # can be changed to mode = scanMode.monitor
tempSettleTime = 30 # time for settling at each temperature step
fieldSettleTime = 0 # time for settling at each field step
highTemp = 4 # for FC before changing field heat to this temperature, also for ZFC before new temperature
lowTemp = 1.6 # for FW before changing field cool to this temperature
highTempSettleTime = 30 # time for settling at max high temperature
lowTempSettleTime = 90 # time for settling at minimum low temperature
firstTempSettleTime = 30 # time for settling at first measurement point after changing temperature
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
            
            for theta in [-2.,0.,2.,4.,6.,8.]:
                log('driving rotation=' + str(theta))
                sics.drive('samthet', theta)
                sleep(thetaSettleTime)
                log('start counting')
                quokka.scan(mode, preset)

    log('driving magnet1_driveable=' + str(0))
    sics.drive('ma1_magnet_setpoint', 0)

def scan_temp_field_ZFC(measurementList, mode, preset, tempSettleTime = 1, fieldSettleTime = 1):
    for temp,fieldList in measurementList:
        log('driving magnet1_driveable=' + str(0))
        sics.drive('ma1_magnet_setpoint', 0) 
        log('waiting for field to settle')
        sleep(fieldSettleTime)
        log('driving tc1_driveable=' +  str(highTemp))
        sics.drive('tc1_driveable', highTemp)
        log('waiting for temperature to settle')
        sleep(highTempSettleTime)        
        log('driving tc1_driveable=' + str(temp))
        sics.drive('tc1_driveable', temp)
        log('waiting for temperature to settle')
        sleep(firstTempSettleTime)
        
        for i,field in enumerate(fieldList):
            log(str(field))
            log('driving magnet1_driveable=' + str(field))
            sics.drive('ma1_magnet_setpoint', field)
            log('waiting for field to settle')
            sleep(fieldSettleTime)
            
            for theta in [-2.,0.,2.,4.,6.,8.]:
                log('driving rotation=' + str(theta))
                sics.drive('samthet', theta)
                sleep(thetaSettleTime)
                log('start counting')
                quokka.scan(mode, preset)

def scan_temp_field_FW(measurementList, mode, preset, tempSettleTime = 1, fieldSettleTime = 1):
    for field,tempList in measurementList:
        log('driving tc1_driveable=' +  str(highTemp))
        sics.drive('tc1_driveable', highTemp)
        log('waiting for temperature to settle')
        sleep(highTempSettleTime)
        log('driving magnet1_driveable=' + str(0))
        sics.drive('ma1_magnet_setpoint', 0) 
        log('waiting for field to settle')
        sleep(fieldSettleTime)
        log('driving tc1_driveable=' +  str(lowTemp))
        sics.drive('tc1_driveable', lowTemp)
        log('waiting for temperature to settle')
        sleep(lowTempSettleTime)        
        log('driving magnet1_driveable=' + str(field))
        sics.drive('ma1_magnet_setpoint', field)
        log('waiting for field to settle')
        sleep(fieldSettleTime)
        
        for i,temp in enumerate(tempList):
            log(str(temp))
            sics.drive('tc1_driveable', temp)         
            log('waiting for temperature to settle')
            if i ==0:
                sleep(firstTempSettleTime)
            else:
                sleep(tempSettleTime)
            
            for theta in [-2.,0.,2.,4.,6.,8.]:
                log('driving rotation=' + str(theta))
                sics.drive('samthet', theta)
                sleep(thetaSettleTime)
                log('start counting')
                quokka.scan(mode, preset)

                     
            
# list for measurements using the FC protocol
listFC_temp = [3.3,3.2,3.1]
listFC = [
            (0.250, listFC_temp)
        ]

# list for measurements using the ZFC protocol
listZFC_fields = [0,0.075,0.125,0.150,0.20,0.25,0.30,0.35]
listZFC = [
           (2.90,listZFC_fields),
           (2.50,listZFC_fields),
           (2.20,listZFC_fields),
           (1.60,listZFC_fields)
        ]

# list for measurements using the FW protocol
listFW_temp = [1.6,1.8,2.,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.,3.1,3.2,3.3]
listFW = [
            (0.000, listFW_temp),
            (0.250, listFW_temp),
            (0.300, listFW_temp),
            (0.350, listFW_temp)
        ]

### from here actual scans are defined
#log('experiment started')

#scan_temp_field_FC(listFC, mode, measurementTime, tempSettleTime, fieldSettleTime)
scan_temp_field_FW(listFW, mode, measurementTime, tempSettleTime, fieldSettleTime)
scan_temp_field_ZFC(listZFC, mode, measurementTime, tempSettleTime, fieldSettleTime)
#scan_temp_helical_FW(listHelicalFW_temp, mode, measurementTime, tempSettleTime, fieldSettleTime)
#scan_theta(wideThetaList, mode, measurementTime)

######
#log('experiment finished')
