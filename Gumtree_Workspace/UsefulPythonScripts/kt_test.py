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

#    sics.drive('nvs_lambda', 4.55)
    sleep(0.1)
    #sics.drive('apx', -23)
    sleep(0.1)
    scan_att_katy(240, 30, 4, [30, 60, 1200, 2400])
    sics.drive('att', 300)
    
    
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