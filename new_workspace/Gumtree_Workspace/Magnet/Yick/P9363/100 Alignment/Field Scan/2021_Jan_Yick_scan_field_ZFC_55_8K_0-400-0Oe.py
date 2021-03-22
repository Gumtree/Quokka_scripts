histmem preset 60
histmem mode time

#-----------------------------------------------------------------
#field sweep at 4K 

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 4
wait 10

hset /sample/tc1/control/tolerance1 0.2

drive tc1_driveable 53
wait 10

drive tc1_driveable 55.8
wait 10

drive ma1_setpoint 0
wait 10

newfile HISTOGRAM_XY
drive ma1_setpoint 0
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 50
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 75
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 100
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 125
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 150
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 175
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 200
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 225
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 250
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 275
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 300
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 275
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 250
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 225
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 200
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 175
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 150
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 125
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 100
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 75
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 50
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 0
histmem start block
save
histmem stop
