#ZFC 4 K field Sweep 80 min scans

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

run tc1_driveable 4
drive tc1_driveable2 4
wait 30

#MEASURE TRANSMISSION at base
run att 150
wait 10
drive bsx 138
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
histmem stop
drive bsx 38
run att 0
wait 10

#80 minute scans
histmem mode time
histmem preset 4800

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

#MEASURE TRANSMISSION
run att 150
wait 10
drive bsx 138
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
histmem stop
drive bsx 38
run att 0
wait 10

#80 minute scans
histmem mode time
histmem preset 4800

run ma1_magnet_setpoint 0.035
wait 240
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.2
wait 240
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

#5 minute scans
histmem mode time
histmem preset 300

run ma1_magnet_setpoint 0.22
wait 240
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.24
wait 240
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.26
wait 240
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

run ma1_magnet_setpoint 0.28
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
wait 30

#80 minute scans
histmem mode time
histmem preset 4800

#120 K Background Scan
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

#MEASURE TRANSMISSION
run att 150
wait 10
drive bsx 138
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
histmem stop
drive bsx 38
run att 0
wait 10

#Prepare for next user
run tc1_driveable2 200
drive tc1_driveable 200
