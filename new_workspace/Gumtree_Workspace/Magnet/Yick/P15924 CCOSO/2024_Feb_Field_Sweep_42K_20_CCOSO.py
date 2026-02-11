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

#Measure a transmission at base (2K)
run att 150
wait 20
drive bsx 138
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
histmem stop
drive bsx 38
run att 0
wait 20

#Heat to set temperature
run tc1_driveable 42
drive tc1_driveable2 42
wait 60

histmem mode time
histmem preset 300

#magnet 0
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

run ma1_magnet_setpoint 0.03
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

run ma1_magnet_setpoint 0.07
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

run ma1_magnet_setpoint 0.09
wait 240
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.1
wait 240
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.15
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

run ma1_magnet_setpoint 0.30
wait 240
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

#reset

run ma1_magnet_setpoint 0
run tc1_driveable2 120
drive tc1_driveable 120
wait 60

#Reset to base (2K)
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