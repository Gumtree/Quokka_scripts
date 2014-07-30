log('starting')
value = 100
sics.drive('magnet1_setpoint', value)
log('finished ' + str(value))
sleep(1)
value = 0
sics.drive('magnet1_setpoint', value)
log('finished ' + str(value))
