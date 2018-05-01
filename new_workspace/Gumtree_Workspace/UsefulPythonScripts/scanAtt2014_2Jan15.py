from time import sleep
from gumpy.commons import sics


def multi_run():
#    sics.drive('att', 300)
#    sics.drive('nvs_lambda', 10)
#    sleep(0.1)
#    scan_att_katy(120, 30, 5, [1200 , 1200, 1800, 3600, 7200])
#    sics.drive('att', 330)
#    sics.drive('nvs_lambda', 10)
#    sleep(0.1)
#    sleep(0.1)
#    scan_att_katy(210, 30, 5, [1200 , 600, 1200, 1800, 3600])
#    sics.drive('att', 330)

#    sics.drive('att', 330)
#    sics.drive('nvs_lambda', 11)
#    sleep(0.1)
#    sleep(0.1)    
#    sleep(0.1)
#    scan_att_katy(180, 30, 6, [1200 , 600, 1200, 1800, 3600, 3600])
#    sics.drive('att', 330)

    #sics.drive('nvs_lambda', 5)
    sleep(0.1)
    #sics.drive('apx', -2.85)
    sleep(0.1)
    scan_att_katy(300, 30, 2, [900, 3600])
    #sics.drive('att', 300)
    
    #sics.drive('att', 330)
    #sics.drive('nvs_lambda', 12)
    #sics.drive('apx', -2.6)
    #sleep(0.1)   
    #sleep(0.1)
    #scan_att_katy(90, 30, 5, [300, 600, 1200, 3600, 7200])
    #sics.drive('att', 330)
    
    #sics.drive('apx', 0)
    #sleep(0.1)   
    #sleep(0.1)
    #scan_att_katy(210, 30, 5, [300, 600, 1200, 3600, 7200])
    #sics.drive('att', 330)
    
    #sics.drive('nvs_lambda', 2.55)
    #sleep(0.1)
    #sics.drive('apx', -2.85)
    #sleep(0.1)
    #scan_att_katy(0, 30, 4, [300, 600, 1200, 3600])
    #sics.drive('att', 300)
    
    #sics.drive('att', 330)
    #sics.drive('nvs_lambda', 12)
    #sics.drive('apx', -2.6)
    #sleep(0.1)   
    #sleep(0.1)
    #scan_att_katy(90, 30, 5, [300, 600, 1200, 3600, 7200])
    #sics.drive('att', 330)
    
    #sics.drive('apx', 0)
    #sleep(0.1)   
    #sleep(0.1)
    #scan_att_katy(210, 30, 5, [300, 600, 1200, 3600, 7200])
    #sics.drive('att', 330)
    
    
def scan_att_katy(start_att, att_step, \
                  number_scan, count_time = None):
    for i in xrange(number_scan) :
        pos = start_att + att_step * i
        driveAtt(pos)
        print 'start scanning for ' + str(count_time[i]) + ' counts'
        scan(scanMode.time, dataType.HISTOGRAM_XY, count_time[i], 'true')
        sleep(1)
        
def run():
    multi_run()