histmem preset 60
histmem mode time

newfile HISTOGRAM_XY
drive ma1_setpoint 950
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 1000
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 1050
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 1100
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 1150
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 1200
histmem start block
save
histmem stop
