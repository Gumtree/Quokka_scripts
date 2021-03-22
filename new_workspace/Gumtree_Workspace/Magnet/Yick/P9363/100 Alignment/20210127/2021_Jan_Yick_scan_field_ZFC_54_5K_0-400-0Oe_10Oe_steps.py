histmem preset 60
histmem mode time

#-----------------------------------------------------------------
#field sweep at 4K 

hset /sample/tc1/control/tolerance1 1

# drive ma1_setpoint 0
# drive tc1_driveable 120
# wait 10

# drive tc1_driveable 4
# wait 10

# hset /sample/tc1/control/tolerance1 0.2

# drive tc1_driveable 50

# drive tc1_driveable 53

# drive tc1_driveable 54

# drive tc1_driveable 54.2
# wait 10

drive tc1_driveable 54.5
wait 10

drive ma1_setpoint 0
wait 10

newfile HISTOGRAM_XY
drive ma1_setpoint 0
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 20
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 50
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 70
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 80
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 90
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 100
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 110
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 120
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 130
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 140
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 150
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 160
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 170
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 180
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 190
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 200
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 210
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 220
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 230
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 240
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 250
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 260
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 270
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 280
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 290
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 300
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 310
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 320
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 330
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 340
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 350
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 360
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 370
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 380
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 390
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 400
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 390
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 380
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 370
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 360
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 350
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 340
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 330
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 320
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 310
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 300
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 290
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 280
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 270
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 260
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 250
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 240
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 230
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 220
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 210
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 200
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 190
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 180
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 170
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 160
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 150
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 140
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 130
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 120
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 110
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 100
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 90
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 80
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 70
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 50
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 40
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 30
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 20
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 10
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 0
histmem start block
save
histmem stop
