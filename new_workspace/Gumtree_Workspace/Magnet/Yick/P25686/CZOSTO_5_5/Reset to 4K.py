#Reset to base temperature
hset /sample/ma1/magnet/pressure_setpoint 15
run tc1_driveable 4
drive tc1_driveable2 4
wait 30
hset /sample/ma1/magnet/pressure_setpoint 10
wait 30
hset /sample/ma1/magnet/pressure_setpoint 7
wait 30
hset /sample/ma1/magnet/pressure_setpoint 5
wait 30
run tc1_driveable 4
drive tc1_driveable2 4
wait 30
hset /sample/ma1/magnet/pressure_setpoint 3
wait 30
drive tc1_driveable2 4
wait 30