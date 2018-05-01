def driveTesla(val, speed, wait_sec):
    sics.execute('oxfordseths on')
    time.sleep(35)
    sics.execute('oxfordsetrate ' + str(speed))
    sics.execute('oxfordsetfield ' + str(val))
    time.sleep(wait_sec)
    sics.execute('oxfordseths off')
    time.sleep(35)
    

