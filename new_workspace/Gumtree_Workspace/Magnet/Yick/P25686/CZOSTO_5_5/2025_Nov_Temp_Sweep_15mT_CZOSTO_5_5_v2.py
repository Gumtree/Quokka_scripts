#0.015 T Temperature Sweep

hset /sample/ma1/magnet/pressure_setpoint 15
run tc1_driveable 4
drive tc1_driveable2 4
wait 30
hset /sample/ma1/magnet/pressure_setpoint 10
wait 30
hset /sample/ma1/magnet/pressure_setpoint 7
wait 30
hset /sample/ma1/magnet/pressure_setpoint 5
wait 30

run tc1_driveable 4
drive tc1_driveable2 4
wait 30

hset /sample/ma1/magnet/pressure_setpoint 3
wait 30

drive tc1_driveable2 4
wait 30

#Mag Field 0.04 T
drive ma1_magnet_setpoint 0.015
wait 10

#Scan Settings
histmem mode time
histmem preset 180

#Scan at 4 K
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
drive tc1_driveable2 10
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 15
drive tc1_driveable2 15
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 20
drive tc1_driveable2 20
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
drive tc1_driveable2 25
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 30
drive tc1_driveable2 30
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 35
drive tc1_driveable2 35
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
drive tc1_driveable2 40
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 41
drive tc1_driveable2 41
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 42
drive tc1_driveable2 42
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
drive tc1_driveable2 43
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 44
drive tc1_driveable2 44
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 45
drive tc1_driveable2 45
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
drive tc1_driveable2 46
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 47
drive tc1_driveable2 47
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 48
drive tc1_driveable2 48
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 49
drive tc1_driveable2 49
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 50
drive tc1_driveable2 50
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 51
drive tc1_driveable2 51
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52
drive tc1_driveable2 52
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53
drive tc1_driveable2 53
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54
drive tc1_driveable2 54
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
drive tc1_driveable2 55
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56
drive tc1_driveable2 56
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57
drive tc1_driveable2 57
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
drive tc1_driveable2 58
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 59
drive tc1_driveable2 59
wait 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 60
drive tc1_driveable2 60
wait 30
histmem start block
save
histmem stop

#Reset to 120 K
#run tc1_driveable 120
drive ma1_magnet_setpoint 0
wait 10
drive tc1_driveable2 120
wait 10