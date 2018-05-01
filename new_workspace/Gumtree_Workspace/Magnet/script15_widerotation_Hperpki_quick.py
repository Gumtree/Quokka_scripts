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
lowTempSettleTime = 60 # time for settling at minimum low temperature
firstTempSettleTime = 30 # time for settling at first measurement point after changing temperature
firstFieldSettleTime = 0 # time for settling at first measurement point after changing field
thetaSettleTime = 5 # time for settling after changing theta
measurementTime = 20 # time for each measurement

  
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
   
def scan_temp_helical_FW(tempList, mode, preset, tempSettleTime = 1, fieldSettleTime = 1):
    log('driving magnet1_driveable=' + str(0))
    sics.drive('ma1_magnet_setpoint', 0) 
    log('waiting for field to settle')
    sleep(fieldSettleTime)
    log('driving tc1_driveable=' +  str(lowTemp))
    sics.drive('tc1_driveable', lowTemp)
    log('waiting for temperature to settle')
    sleep(lowTempSettleTime) 
    for i,temp in enumerate(tempList):
        log(str(temp))
        sics.drive('tc1_driveable', temp)         
        log('waiting for temperature to settle')

        if i ==0:
            sleep(firstTempSettleTime)
        else:
            sleep(tempSettleTime)
        
        for theta in [0.,6.]:
            log('driving rotation=' + str(theta))
            sics.drive('samthet', theta)
            sleep(thetaSettleTime)
            log('start counting')
            quokka.scan(mode, preset)
            
            
def scan_theta(thetaList, mode, preset):
    for theta in thetaList:
        log('driving rotation=' + str(theta))
        sics.drive('samthet', theta)
        sleep(thetaSettleTime)
        log('start counting')
        quokka.scan(mode, preset)
    
                     
            
# list for measurements using the FC protocol
listFC_temp = [3.0,2.9,2.8,2.7,2.6,2.5,2.4,2.3,2.2,2.1,2.0,1.8,1.6]
listFC = [
            (0.000, listFC_temp),
            (0.050, listFC_temp),
            (0.075, listFC_temp),
            (0.100, listFC_temp),
            (0.125, listFC_temp),
            (0.150, listFC_temp),
            (0.175, listFC_temp),
            (0.200, listFC_temp),
            (0.250, listFC_temp),
            (0.300, listFC_temp),
            (0.350, listFC_temp),
            (0.400, listFC_temp)
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

# list for checking transition temp of helical phase
listHelicalFW_temp = [1.6, 1.7, 1.8, 1.9, 2., 2.1, 2.2, 2.3, 2.4,2.5,2.6,2.7,2.8,2.9,3.0]

wideThetaList = [-8.,-6.,-4.,-2.,0.,2.,4.,6.,8.,10.]

### from here actual scans are defined
#log('experiment started')

#scan_temp_field_FC(listFC, mode, measurementTime, tempSettleTime, fieldSettleTime)
#scan_temp_field_ZFC(listZFC, mode, measurementTime, tempSettleTime, fieldSettleTime)
#scan_temp_field_FW(listFW, mode, measurementTime, tempSettleTime, fieldSettleTime)
#scan_temp_helical_FW(listHelicalFW_temp, mode, measurementTime, tempSettleTime, fieldSettleTime)
scan_theta(wideThetaList, mode, measurementTime)

######
#log('experiment finished')
