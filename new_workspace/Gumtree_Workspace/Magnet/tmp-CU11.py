histmem preset 60
histmem mode time


#==============================================================================================
# drive tc1_driveable 60
# drive ma1_setpoint 0
# wait 10

newfile HISTOGRAM_XY
drive samthet -3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive samthet -2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive samthet -1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive samthet 0
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive samthet 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive samthet 2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive samthet 3
histmem start block
save
histmem stop
