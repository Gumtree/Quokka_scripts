histmem preset 30
histmem mode time


#Searching for the Skyx
#-----------------------------------------------------------------
#temperature sweep at 200 Oe from 4K 

drive tc1_driveable 4
wait 10

# Set magnetic field

drive ma1_setpoint 200
wait 10

drive tc1_driveable 45
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 48
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
