from gumpy.commons import sics
#from gumpy.quokka.quokka import *
from time import sleep


######################
# GLOBAL settings
mode = "time" # can be changed to mode = scanMode.monitor
tempSettleTime = 60 # time for settling at each temperature step
fieldSettleTime = 0 # time for settling at each field step
highTemp = 5 # for FC before changing field heat to this temperature, also for ZFC before new temperature
lowTemp = 2 # for FW before changing field cool to this temperature
highTempSettleTime = 60 # time for settling at max high temperature
lowTempSettleTime = 60 # time for settling at minimum low temperature
firstTempSettleTime = 60 # time for settling at first measurement point after changing temperature
firstFieldSettleTime = 0 # time for settling at first measurement point after changing field
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
            log(str(temp))
            sics.drive('tc1_driveable', temp)         
            log('waiting for temperature to settle')
            if i ==0:
                sleep(firstTempSettleTime)
            else:
                sleep(tempSettleTime)
            
            log('start counting')
            quokka.scan(mode, preset)

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
            if i == 0:
                sleep(firstFieldSettleTime)
            else:
                sleep(fieldSettleTime)
            
            log('start counting')
            quokka.scan(mode, preset)

def scan_temp_field_FW(measurementList, mode, preset, tempSettleTime = 1, fieldSettleTime = 1):
    for field,tempList in measurementList:
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
            
            log('start counting')
            quokka.scan(mode, preset)
            
            
# list for measurements using the FC protocol
listFC_temp = [4,3.75,3.6,3.5,3.25,3.,2.75,2.5,2.25,2]
listFC = [
            (0.00, listFC_temp),
            (0.05, listFC_temp),
            (0.08, listFC_temp),
            (0.09, listFC_temp),
            (0.10, listFC_temp),
            (0.15, listFC_temp),
            (0.20, listFC_temp),
            (0.25, listFC_temp),
            (0.30, listFC_temp),
            (0.35, listFC_temp),
            (0.40, listFC_temp)
        ]

# list for measurements using the ZFC protocol
listZFC_fields = [0,0.05,0.08,0.09,0.10,0.15,0.20,0.25,0.30,0.35,0.40]
listZFC = [
           (4.00,listZFC_fields),
           (3.75,listZFC_fields),
           (3.60,listZFC_fields),
           (3.50,listZFC_fields),
           (3.25,listZFC_fields),
           (3.00,listZFC_fields),
           (2.75,listZFC_fields),
           (2.50,listZFC_fields)
        ]

# list for measurements using the FW protocol
listFW_temp = [2,2.25,2.5,2.75,3.,3.25,3.5,3.6,3.75,4]
listFW = [
            (0.00, listFW_temp),
            (0.05, listFW_temp),
            (0.08, listFW_temp),
            (0.09, listFW_temp),
            (0.10, listFW_temp),
            (0.15, listFW_temp),
            (0.20, listFW_temp),
            (0.25, listFW_temp),
            (0.30, listFW_temp),
            (0.35, listFW_temp),
            (0.40, listFW_temp)
        ]


### from here actual scans are defined
#log('experiment started')

scan_temp_field_FC(listFC, mode, measurementTime, tempSettleTime, fieldSettleTime)
scan_temp_field_ZFC(listZFC, mode, measurementTime, tempSettleTime, fieldSettleTime)
scan_temp_field_FW(listFW, mode, measurementTime, tempSettleTime, fieldSettleTime)

######
#log('experiment finished')
