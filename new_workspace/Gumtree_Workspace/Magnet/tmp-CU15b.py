histmem preset 120
histmem mode time

#==============================================================================================
# drive tc1_driveable 60
# drive ma1_setpoint   0
# wait 10

#==============================================================================================

newfile HISTOGRAM_XY
drive ma1_setpoint 850
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 800
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 750
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 700
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 650
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 600
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 550
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 500
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 450
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 400
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 350
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 300
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 250
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 200
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 150
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 100
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 50
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 0
wait 1
histmem start block
save
histmem stop