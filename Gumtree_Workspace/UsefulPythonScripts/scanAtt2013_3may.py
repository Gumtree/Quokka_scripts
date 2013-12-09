from time import sleep
from gumpy.commons import sics


def multi_run():
    sics.drive('att', 300)
    sics.drive('nvs_lambda', 8)
    sleep(0.1)
    sics.drive('apx', 0)
    sleep(0.1)
    scan_att_katy(0, 30, 2, [10 , 10])
    sics.drive('att', 300)

    sics.drive('nvs_lambda', 8)
    sleep(0.1)
    sics.drive('apx', -250)
    sleep(0.1)
    scan_att_katy(240, 30, 2, [10 , 10])
    sics.drive('att', 300)

    sics.drive('nvs_lambda', 9)
    sleep(0.1)
    sics.drive('apx', 0)
    sleep(0.1)
    scan_att_katy(0, 30, 4, [1200 , 1200, 1800, 3600])
    sics.drive('att', 300)

    sics.drive('nvs_lambda', 9)
    sleep(0.1)
    sics.drive('apx', -250)
    sleep(0.1)
    scan_att_katy(90, 30, 7, [1200 , 1200, 1800, 1800, 3600, 7200, 14000])
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