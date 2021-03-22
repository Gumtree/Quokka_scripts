histmem preset 60
histmem mode time

#drive ma1_setpoint 0
#drive tc1_driveable 90
#wait 10


#-----------------------------------------------------------------
#temperature sweep at 1100 Oe from 4K 

hset /sample/tc1/control/tolerance1 1

run ma1_setpoint 0
run tc1_driveable 120
wait 100

drive tc1_driveable 4
wait 10

drive ma1_setpoint 200
wait 10

hset /sample/tc1/control/tolerance1 0.2


newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 12
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 14
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 18
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 20
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 24
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 26
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 32
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 36
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 38
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 42
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 44
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 48
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 50
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 50.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 50.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 50.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 51.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 51.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 51.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 59
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 60
histmem start block
save
histmem stop

drive ma1_setpoint 0
drive tc1_driveable 90
wait 10
