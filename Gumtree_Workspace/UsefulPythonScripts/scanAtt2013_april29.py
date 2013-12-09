from time import sleep
START_ATT = 270
ATT_STEP_SIZE = +30
COUNT_TIME = [10 , 20]
NUMBER_OF_SCAN = 2

def scan_att_katy(start_att = START_ATT, att_step = ATT_STEP_SIZE, \
                  number_scan = NUMBER_OF_SCAN, count_time = None):
    if count_time is None:
        count_time = COUNT_TIME
    for i in xrange(number_scan) :
        pos = start_att + att_step * i
        driveAtt(pos)
        print 'start scanning for ' + str(count_time[i]) + ' counts'
        scan(scanMode.time, dataType.HISTOGRAM_XY, count_time[i], 'true')
        sleep(1)
        
def run():
    scan_att_katy()