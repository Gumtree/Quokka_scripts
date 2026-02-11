#script took 2hr 18 min 16 sec 20/2/24 

run tc2_pres3_setpoint 20
run tc1_driveable 4
drive tc1_driveable2 4

run tc2_pres3_setpoint 4

run ma1_magnet_setpoint 0.035
wait 240

histmem mode time
histmem preset 300

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 10
drive tc1_driveable2 10
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 15
drive tc1_driveable2 15
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 20
drive tc1_driveable2 20
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 25
drive tc1_driveable2 25
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 30
drive tc1_driveable2 30
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 35
drive tc1_driveable2 35
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 40
drive tc1_driveable2 40
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 41
drive tc1_driveable2 41
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 42
drive tc1_driveable2 42
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 43
drive tc1_driveable2 43
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 44
drive tc1_driveable2 44
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 45
drive tc1_driveable2 45
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 46
drive tc1_driveable2 46
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 47
drive tc1_driveable2 47
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 48
drive tc1_driveable2 48
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 48.5
drive tc1_driveable2 48.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 49
drive tc1_driveable2 49
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 49.5
drive tc1_driveable2 49.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 50
drive tc1_driveable2 50
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 50.5
drive tc1_driveable2 50.5
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 51
drive tc1_driveable2 51
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 52
drive tc1_driveable2 52
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 53
drive tc1_driveable2 53
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 54
drive tc1_driveable2 54
wait 10
histmem start block
save
histmem stop

#newfile HISTOGRAM_XY
#drive tc1_driveable 54.5
#drive tc1_driveable2 54.5
#wait 10
#histmem start block
#save
#histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 55
drive tc1_driveable2 55
wait 10
histmem start block
save
histmem stop

#newfile HISTOGRAM_XY
#drive tc1_driveable 55.5
#drive tc1_driveable2 55.5
#wait 10
#histmem start block
#save
#histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 56
drive tc1_driveable2 56
wait 10
histmem start block
save
histmem stop

#newfile HISTOGRAM_XY
#drive tc1_driveable 56.5
#drive tc1_driveable2 56.5
#wait 10
#histmem start block
#save
#histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 57
drive tc1_driveable2 57
wait 10
histmem start block
save
histmem stop

#newfile HISTOGRAM_XY
#drive tc1_driveable 57.5
#drive tc1_driveable2 57.5
#wait 10
#histmem start block
#save
#histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
drive tc1_driveable2 58
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 59
drive tc1_driveable2 59
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 60
drive tc1_driveable2 60
wait 10
histmem start block
save
histmem stop

#reset

run ma1_magnet_setpoint 0
run tc1_driveable 120
drive tc1_driveable2 120

