histmem preset 60
histmem mode time


#H-T Phase Diagram
#-----------------------------------------------------------------
#temperature sweep at 0 Oe from 4K 

#hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 5
wait 10

hset /sample/tc1/control/tolerance1 0.2

###### Set Field!!!! ######

drive ma1_setpoint 200
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 13
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 19
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 31
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 37
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 49
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 50
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 50.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 51
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 51.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.7
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