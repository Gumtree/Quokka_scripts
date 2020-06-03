histmem preset 60
histmem mode time


#H-T Phase Diagram
#-----------------------------------------------------------------
#temperature sweep at 0 Oe from 12K --- Field cooled at 200 Oe

drive tc1_driveable 80
drive ma1_setpoint 200
wait 100
drive tc1_driveable 12
wait 10
drive ma1_setpoint 0
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 49
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 49.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 60
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 50 Oe from 12K --- Field cooled at 200 Oe

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 50
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 49
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 49.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 60
wait 10
histmem start block
save
histmem stop
#-----------------------------------------------------------------
#temperature sweep at 100 Oe from 12K --- Field cooled at 200 Oe

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 100
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 49
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 49.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 60
wait 10
histmem start block
save
histmem stop
#-----------------------------------------------------------------
#temperature sweep at 150 Oe from 12K --- Field cooled at 200 Oe

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 150
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 49
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 49.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 60
wait 10
histmem start block
save
histmem stop
#-----------------------------------------------------------------
#temperature sweep at 200 Oe from 12K --- Field cooled at 200 Oe

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 200
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 49
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 49.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 60
wait 10
histmem start block
save
histmem stop
#-----------------------------------------------------------------
#temperature sweep at 250 Oe from 12K --- Field cooled at 200 Oe

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 250
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 49
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 49.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 60
wait 10
histmem start block
save
histmem stop
#-----------------------------------------------------------------
#temperature sweep at 300 Oe from 12K --- Field cooled at 200 Oe

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 300
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 49
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 49.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 60
wait 10
histmem start block
save
histmem stop
#-----------------------------------------------------------------
#temperature sweep at 350 Oe from 12K --- Field cooled at 200 Oe

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 350
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 49
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 49.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 60
wait 10
histmem start block
save
histmem stop
#-----------------------------------------------------------------
#temperature sweep at 400 Oe from 12K --- Field cooled at 200 Oe

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 400
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 49
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 49.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 51.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 52.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 53.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 54.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 55.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 56.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.3
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.6
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 57.9
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.2
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 58.8
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.1
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.4
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 59.7
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 60
wait 10
histmem start block
save
histmem stop


#H-T Phase Diagram
#-----------------------------------------------------------------
#temperature sweep at 450 Oe from 12K 

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 450
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 500 Oe from 12K 

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 500
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 550 Oe from 12K 

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 550
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 600 Oe from 12K 

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 600
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 650 Oe from 12K 

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 650
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 700 Oe from 12K 

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 700
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 750 Oe from 12K 

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 750
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 800 Oe from 12K 

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 800
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 850 Oe from 12K 

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 850
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 900 Oe from 12K 

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 900
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 950 Oe from 12K 

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 950
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 1000 Oe from 12K 

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 1000
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 1050 Oe from 12K 

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 1050
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 1100 Oe from 12K 

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 1100
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 1150 Oe from 12K 

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 1150
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 1200 Oe from 12K 

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 1200
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 1250 Oe from 12K 

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 1250
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 1300 Oe from 12K 

drive tc1_driveable 80
drive ma1_setpoint 200
wait 10
drive tc1_driveable 12
wait 10
drive ma1_setpoint 1300
wait 10

newfile HISTOGRAM_XY
run tc1_driveable 12
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 14
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 16
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 18
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 22
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 24
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 26
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 28
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 32
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 34
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 36
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 38
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
run tc1_driveable 50
wait 10
histmem start block
save
histmem stop

