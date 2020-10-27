histmem preset 60
histmem mode time


#H-T Phase Diagram
#-----------------------------------------------------------------
#temperature sweep at 0 Oe from 4K 

drive tc1_driveable 80
drive ma1_setpoint 0
wait 10
drive tc1_driveable 4
wait 10

# Set magnetic field

drive ma1_setpoint 0
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 12
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 14
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 18
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 20
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 24
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 26
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 32
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 36
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 38
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 42
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 44
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
histmem start block
save
histmem stop

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
drive tc1_driveable 52.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 59
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 59.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 60
histmem start block
save
histmem stop

drive tc1_driveable 90
drive ma1_setpoint 0
wait 10
