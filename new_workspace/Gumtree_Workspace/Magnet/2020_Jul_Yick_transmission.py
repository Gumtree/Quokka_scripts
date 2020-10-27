histmem preset 120
histmem mode time

drive tc1_driveable 90
drive ma1_setpoint 0

run att 180 
reldrive bsx 100

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

reldrive bsx -100


