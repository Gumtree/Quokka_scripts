
#==============================================================================================
drive tc1_driveable 60
drive ma1_setpoint   0
wait 10

drive tc1_driveable 4

newfile HISTOGRAM_XY
drive ma1_setpoint 0
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 10
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 20
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 30
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 40
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
drive ma1_setpoint 60
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 70
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 80
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 90
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
drive ma1_setpoint 110
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 120
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 130
wait 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 140
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

