from time import sleep
from gumpy.commons import sics


def multi_run():
    sics.drive('nvs_lambda', 4.505)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 120, 'true')    
    sleep(0.1)
    
    sics.drive('nvs_lambda', 4.6)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 120, 'true')    
    sleep(0.1)

    sics.drive('nvs_lambda', 4.7)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 120, 'true')    
    sleep(0.1)
    
    sics.drive('nvs_lambda', 4.8)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 120, 'true')    
    sleep(0.1)

    sics.drive('nvs_lambda', 4.9)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 120, 'true')    
    sleep(0.1)

    sics.drive('nvs_lambda', 5)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 120, 'true')    
    sleep(0.1)
    
    sics.drive('nvs_lambda', 5.1)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 120, 'true')    
    sleep(0.1)
 
    sics.drive('nvs_lambda', 5.2)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 120, 'true')    
    sleep(0.1)
    
    sics.drive('nvs_lambda', 5.3)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 120, 'true')    
    sleep(0.1)
 
    sics.drive('nvs_lambda', 5.4)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 120, 'true')    
    sleep(0.1)
 
    sics.drive('nvs_lambda', 5.5)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 120, 'true')  
    sleep(0.1)
    
    sics.drive('nvs_lambda', 5.6)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 120, 'true')  
    sleep(0.1)

    sics.drive('nvs_lambda', 5.7)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 120, 'true')  
    sleep(0.1)

    sics.drive('nvs_lambda', 5.8)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 120, 'true')  
    sleep(0.1)

    sics.drive('nvs_lambda', 5.9)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 120, 'true')  
    sleep(0.1)

    sics.drive('nvs_lambda', 6)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 120, 'true')  
    sleep(0.1)

    sics.drive('nvs_lambda', 6.5)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 120, 'true')  
    sleep(0.1)

    sics.drive('nvs_lambda', 7)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 240, 'true')  
    sleep(0.1)
    
    sics.drive('nvs_lambda', 7.5)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 240, 'true')  
    sleep(0.1)
  
    sics.drive('nvs_lambda', 8)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 240, 'true')  
    sleep(0.1)
    
    sics.drive('nvs_lambda', 9)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 240, 'true')  
    sleep(0.1)
    
    sics.drive('nvs_lambda', 10)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 360, 'true')  
    sleep(0.1) 
     
    sics.drive('nvs_lambda', 11)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 360, 'true')  
    sleep(0.1) 
     
    sics.drive('nvs_lambda', 12)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 360, 'true')  
    sleep(0.1) 
    
    sics.drive('nvs_lambda', 17)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 480, 'true')  
    sleep(0.1)
    
    sics.drive('nvs_lambda', 20)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 480, 'true')  
    sleep(0.1)
    
    sics.drive('nvs_lambda', 25)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 480, 'true')  
    sleep(0.1)
    
    sics.drive('nvs_lambda', 40)
    sleep(0.1)
    print 'start scanning for '
    scan(scanMode.time, dataType.HISTOGRAM_XY, 480, 'true')  
    sleep(0.1)
    
def run():
    multi_run()