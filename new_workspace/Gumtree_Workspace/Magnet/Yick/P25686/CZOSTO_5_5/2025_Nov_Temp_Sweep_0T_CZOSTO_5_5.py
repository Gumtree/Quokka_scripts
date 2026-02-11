#0 T Temperature Sweep

#hset /sample/ma1/magnet/pressure_setpoint 20
#run tc1_driveable 2
#drive tc1_driveable2 2
#wait 10
#hset /sample/ma1/magnet/pressure_setpoint 10
#wait 30
#hset /sample/ma1/magnet/pressure_setpoint 7
#wait 30
#hset /sample/ma1/magnet/pressure_setpoint 5
#wait 30

#drive tc1_driveable 4
#drive tc1_driveable2 4
#wait 30

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
drive tc1_driveable 45
drive tc1_driveable2 45
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
drive tc1_driveable2 120
wait 30
#newfile HISTOGRAM_XY
#histmem start block
#save
#histmem stop