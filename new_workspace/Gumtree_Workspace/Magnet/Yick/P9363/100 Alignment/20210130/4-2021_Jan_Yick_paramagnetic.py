histmem preset 600
histmem mode time

drive ma1_setpoint 0
wait 10

drive tc1_driveable 120
wait 10

newfile HISTOGRAM_XY
drive ma1_setpoint 0
histmem start block
save
histmem stop