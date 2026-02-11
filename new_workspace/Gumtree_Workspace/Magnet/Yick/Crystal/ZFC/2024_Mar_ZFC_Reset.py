#ZFC

run ma1_magnet_setpoint -0.015
wait 240
#run tc1_driveable2 120
#drive tc1_driveable 120

run tc2_pres3_setpoint 20
run tc1_driveable 2
drive tc1_driveable2 2
wait 10
run tc2_pres3_setpoint 10
wait 60
run tc2_pres3_setpoint 7
wait 60
run tc2_pres3_setpoint 5
wait 30
run tc1_driveable 4
drive tc1_driveable2 4
