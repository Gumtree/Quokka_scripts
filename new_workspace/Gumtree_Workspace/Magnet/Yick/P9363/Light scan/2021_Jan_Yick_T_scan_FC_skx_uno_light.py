histmem preset 60
histmem mode time


temperature sweep 

hset /sample/tc1/control/tolerance1 1

run ma1_setpoint 0
run tc1_driveable 120
wait 10

drive ma1_setpoint 200
wait 10

run tc1_driveable 4
wait 10

hset /sample/tc1/control/tolerance1 0.2

drive tc1_driveable 50
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 50
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 51
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 59
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 59.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 60
histmem start block
save
histmem stop

