histmem preset 60
histmem mode time


#H-T Phase Diagram
#-----------------------------------------------------------------
#temperature sweep at 0 Oe from 4K 

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 5
wait 10

hset /sample/tc1/control/tolerance1 0.2

###### Set Field!!!! ######

drive ma1_setpoint 0
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 13
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 19
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 31
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 37
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
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
drive tc1_driveable 52.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 59
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 60
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 50 Oe from 4K 

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 5
wait 10

hset /sample/tc1/control/tolerance1 0.2

###### Set Field!!!! ######

drive ma1_setpoint 50
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 13
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 19
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 31
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 37
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
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
drive tc1_driveable 52.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 59
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 60
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 100 Oe from 4K 

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 5
wait 10

hset /sample/tc1/control/tolerance1 0.2

###### Set Field!!!! ######

drive ma1_setpoint 100
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 13
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 19
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 31
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 37
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
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
drive tc1_driveable 52.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 59
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 60
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 150 Oe from 4K 

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 5
wait 10

hset /sample/tc1/control/tolerance1 0.2

###### Set Field!!!! ######

drive ma1_setpoint 150
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 13
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 19
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 31
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 37
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
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
drive tc1_driveable 52.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 59
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 60
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 200 Oe from 4K 

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 5
wait 10

hset /sample/tc1/control/tolerance1 0.2

###### Set Field!!!! ######

drive ma1_setpoint 200
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 13
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 19
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 31
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 37
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
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
drive tc1_driveable 52.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 59
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 60
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 250 Oe from 4K 

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 5
wait 10

hset /sample/tc1/control/tolerance1 0.2

###### Set Field!!!! ######

drive ma1_setpoint 250
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 13
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 19
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 31
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 37
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
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
drive tc1_driveable 52.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 59
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 60
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 300 Oe from 4K 

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 5
wait 10

hset /sample/tc1/control/tolerance1 0.2

###### Set Field!!!! ######

drive ma1_setpoint 300
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 13
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 19
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 31
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 37
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
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
drive tc1_driveable 52.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 59
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 60
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 350 Oe from 4K 

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 5
wait 10

hset /sample/tc1/control/tolerance1 0.2

###### Set Field!!!! ######

drive ma1_setpoint 350
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 13
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 19
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 31
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 37
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
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
drive tc1_driveable 52.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 59
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 60
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 400 Oe from 4K 

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 5
wait 10

hset /sample/tc1/control/tolerance1 0.2

###### Set Field!!!! ######

drive ma1_setpoint 400
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 13
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 19
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 31
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 37
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
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
drive tc1_driveable 52.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.3
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.6
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55.9
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.5
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56.8
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57.7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 59
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 60
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 450 Oe from 4K 

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 5
wait 10

hset /sample/tc1/control/tolerance1 0.2

###### Set Field!!!! ######

drive ma1_setpoint 450
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 13
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 19
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 31
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 37
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 49
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 500 Oe from 4K 

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 5
wait 10

hset /sample/tc1/control/tolerance1 0.2

###### Set Field!!!! ######

drive ma1_setpoint 500
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 13
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 19
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 31
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 37
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 49
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 550 Oe from 4K 

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 5
wait 10

hset /sample/tc1/control/tolerance1 0.2

###### Set Field!!!! ######

drive ma1_setpoint 550
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 13
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 19
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 31
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 37
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 49
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 600 Oe from 4K 

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 5
wait 10

hset /sample/tc1/control/tolerance1 0.2

###### Set Field!!!! ######

drive ma1_setpoint 600
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 13
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 19
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 31
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 37
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 49
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 650 Oe from 4K 

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 5
wait 10

hset /sample/tc1/control/tolerance1 0.2

###### Set Field!!!! ######

drive ma1_setpoint 650
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 13
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 19
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 31
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 37
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 49
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 700 Oe from 4K 

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 5
wait 10

hset /sample/tc1/control/tolerance1 0.2

###### Set Field!!!! ######

drive ma1_setpoint 700
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 13
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 19
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 31
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 37
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 49
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 750 Oe from 4K 

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 5
wait 10

hset /sample/tc1/control/tolerance1 0.2

###### Set Field!!!! ######

drive ma1_setpoint 750
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 13
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 19
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 31
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 37
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 49
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 800 Oe from 4K 

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 5
wait 10

hset /sample/tc1/control/tolerance1 0.2

###### Set Field!!!! ######

drive ma1_setpoint 800
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 13
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 19
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 31
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 37
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 49
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 850 Oe from 4K 

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 5
wait 10

hset /sample/tc1/control/tolerance1 0.2

###### Set Field!!!! ######

drive ma1_setpoint 850
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 13
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 19
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 31
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 37
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 49
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop

#-----------------------------------------------------------------
#temperature sweep at 900 Oe from 4K 

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 5
wait 10

hset /sample/tc1/control/tolerance1 0.2

###### Set Field!!!! ######

drive ma1_setpoint 900
wait 10

newfile HISTOGRAM_XY
drive tc1_driveable 4
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 7
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 13
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 16
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 19
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 22
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 28
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 31
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 34
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 37
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 49
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
histmem start block
save
histmem stop