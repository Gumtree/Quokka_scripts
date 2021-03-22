histmem preset 60
histmem mode time


#Searching for the Skyx
#-----------------------------------------------------------------
#temperature sweep at 200 Oe from 4K 

# Set magnetic field

drive ma1_setpoint 200
wait 10

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
