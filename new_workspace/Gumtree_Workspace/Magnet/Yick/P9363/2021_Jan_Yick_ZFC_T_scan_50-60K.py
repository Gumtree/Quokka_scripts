histmem preset 60
histmem mode time

#drive ma1_setpoint 0
#drive tc1_driveable 90
#wait 10


#-----------------------------------------------------------------
#temperature sweep at 1100 Oe from 4K 

#drive tc1_driveable 4
#wait 10
drive ma1_setpoint 200
wait 10


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
