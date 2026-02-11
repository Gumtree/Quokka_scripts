#ZFC
run tc2_pres3_setpoint 20
run tc1_driveable 2
drive tc1_driveable2 2
wait 300
run tc2_pres3_setpoint 10
wait 60
run tc2_pres3_setpoint 7
wait 60
run tc2_pres3_setpoint 5
wait 30

run tc1_driveable 2
drive tc1_driveable2 2
wait 10

histmem mode time
histmem preset 300

#magnet 0
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

run ma1_magnet_setpoint 0.015
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

run ma1_magnet_setpoint 0.035
wait 240
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.04
wait 240
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.045
wait 240
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.05
wait 240
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.06
wait 240
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.08
wait 240
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.12
wait 240
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.16
wait 240
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.20
wait 240
newfile HISTOGRAM_XY
histmem start block
save
histmem stop


#reset

run ma1_magnet_setpoint 0
run tc1_driveable2 120
drive tc1_driveable 120

