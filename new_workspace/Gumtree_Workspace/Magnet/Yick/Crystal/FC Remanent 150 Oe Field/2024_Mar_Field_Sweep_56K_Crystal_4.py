#ZFC

run tc2_pres3_setpoint 20

run tc1_driveable 2
drive tc1_driveable2 2
wait 10

run tc2_pres3_setpoint 5
wait 300

drive tc1_driveable 4
drive tc1_driveable2 4
wait 60

drive tc1_driveable 56
drive tc1_driveable2 56
wait 60

histmem mode time
histmem preset 600

#magnet 0
#newfile HISTOGRAM_XY
#histmem start block
#save
#histmem stop

run ma1_magnet_setpoint 0.005
wait 240

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.010
wait 240

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.015
wait 240

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.020
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

#reset

run ma1_magnet_setpoint 0
run tc1_driveable2 120
drive tc1_driveable 120

