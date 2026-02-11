#ZFC
run ma1_magnet_setpoint -0.0150
wait 240

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

run tc1_driveable 40
drive tc1_driveable2 40

run tc1_driveable 50
drive tc1_driveable2 50

run tc1_driveable 56
drive tc1_driveable2 56

histmem mode time
histmem preset 300

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint -0.01
wait 240
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint -0.005
wait 240
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0
wait 240

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.005
wait 240

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.01
wait 240

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.02
wait 240

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.025
wait 240

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.03
wait 240

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

#run ma1_magnet_setpoint 0.14
#wait 240

#newfile HISTOGRAM_XY
#histmem start block
#save
#histmem stop

#run ma1_magnet_setpoint 0.2
#wait 240

#newfile HISTOGRAM_XY
#histmem start block
#save
#histmem stop

#reset
run ma1_magnet_setpoint 0
run tc1_driveable2 120
drive tc1_driveable 120