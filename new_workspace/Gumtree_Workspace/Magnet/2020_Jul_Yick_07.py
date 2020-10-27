histmem preset 60
histmem mode time

drive tc1_driveable 90
wait 10
drive ma1_setpoint 0
wait 10


#H-T Phase Diagram for Dark, 0, 200, 450, 500, 650 Oe, FC 0, 200 Oe at 200Oe
#-----------------------------------------------------------------
#temperature sweep at 0 Oe from 4K 

drive tc1_driveable 4
wait 10
drive ma1_setpoint 500
wait 10


newfile HISTOGRAM_XY
drive tc1_driveable 50
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 60
histmem start block
save
histmem stop

drive ma1_setpoint 0
wait 10
drive tc1_driveable 90
wait 10

