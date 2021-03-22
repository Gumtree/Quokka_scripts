histmem preset 60
histmem mode time

#-----------------------------------------------------------------
#field sweep at 4K 

drive tc1_driveable 56
wait 10

drive ma1_setpoint 0
wait 10

newfile HISTOGRAM_XY
drive ma1_setpoint 0
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 50
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 100
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 150
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 200
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 250
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 300
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 350
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 400
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 450
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 500
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 550
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 600
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 650
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 700
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 750
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 800
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 850
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 900
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 950
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 1000
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 1050
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 1100
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 1150
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 1200
histmem start block
save
histmem stop

histmem preset 60
histmem mode time

drive ma1_setpoint 0
wait 10

drive tc1_driveable 120
wait 10

drive tc1_driveable 4
wait 10
