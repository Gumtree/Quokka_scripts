histmem preset 60
histmem mode time


#H-T Phase Diagram
#-----------------------------------------------------------------
#temperature sweep at 900 Oe from 12K --- Field cooled at 200 Oe

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 4
wait 10
drive ma1_setpoint 900
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 10
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 800 Oe from 12K --- Field cooled at 200 Oe

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 4
wait 10
drive ma1_setpoint 800

newfile HISTOGRAM_XY
run tc1_driveable 4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 10
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 700 Oe from 12K --- Field cooled at 200 Oe

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 4
wait 10
drive ma1_setpoint 700
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 10
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 600 Oe from 12K --- Field cooled at 200 Oe

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 4
wait 10
drive ma1_setpoint 600
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 10
wait 10
histmem start block
save
histmem stop


#-----------------------------------------------------------------
#temperature sweep at 500 Oe from 12K --- Field cooled at 200 Oe

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 4
wait 10
drive ma1_setpoint 500
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 10
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 400 Oe from 12K --- Field cooled at 200 Oe

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 4
wait 10
drive ma1_setpoint 400
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 10
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 300 Oe from 12K --- Field cooled at 200 Oe

drive tc1_driveable 4
wait 10
drive ma1_setpoint 300
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 10
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 200 Oe from 12K --- Field cooled at 200 Oe

drive tc1_driveable 4
wait 10
drive ma1_setpoint 200
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 10
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 100 Oe from 12K --- Field cooled at 200 Oe

drive tc1_driveable 4
wait 10
drive ma1_setpoint 100
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 10
wait 10
histmem start block
save
histmem stop

