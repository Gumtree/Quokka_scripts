#ZFC

run ma1_magnet_setpoint 0
run tc1_driveable2 120
drive tc1_driveable 120

run tc2_pres3_setpoint 20

run tc1_driveable 2
drive tc1_driveable2 2
wait 10

run tc2_pres3_setpoint 5
wait 300

drive tc1_driveable 4
drive tc1_driveable2 4
wait 60


drive tc1_driveable 57
drive tc1_driveable2 57