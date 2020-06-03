histmem preset 60
histmem mode time


#H-T Phase Diagram
#-----------------------------------------------------------------
#temperature sweep at 0 Oe from 12K 

drive tc1_driveable 80
drive ma1_setpoint 0
wait 10
drive tc1_driveable 4
wait 10
drive ma1_setpoint 650
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 12
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
histmem start block
save
histmem stop

