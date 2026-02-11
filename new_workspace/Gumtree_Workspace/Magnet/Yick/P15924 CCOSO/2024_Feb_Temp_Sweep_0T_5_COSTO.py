#0 T Temperature Sweep

#run tc2_pres3_setpoint 20
#run tc1_driveable 2
#drive tc1_driveable2 2
#wait 10
#run tc2_pres3_setpoint 10
#wait 60
#run tc2_pres3_setpoint 7
#wait 60
#run tc2_pres3_setpoint 5
#wait 30
#run tc1_driveable 4
#drive tc1_driveable2 4
#wait 30


#Measure a transmission at base
#run att 150
#wait 20
#drive bsx 138
#newfile HISTOGRAM_XY
#histmem mode time
#histmem preset 120
#histmem start block
#save
#histmem stop
#drive bsx 38
#run att 0
#wait 20

#Scan Settings
histmem mode time
histmem preset 300

#Scan at 4 K
newfile HISTOGRAM_XY
wait 10
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
drive tc1_driveable 20
drive tc1_driveable2 20
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
drive tc1_driveable 40
drive tc1_driveable2 40
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
drive tc1_driveable 52
drive tc1_driveable2 52
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

newfile HISTOGRAM_XY
drive tc1_driveable 56
drive tc1_driveable2 56
wait 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive tc1_driveable 58
drive tc1_driveable2 58
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

#Reset to 120 K
run tc1_driveable 120
drive tc1_driveable2 120