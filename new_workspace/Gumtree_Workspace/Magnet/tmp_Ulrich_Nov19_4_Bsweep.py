histmem preset 90
histmem mode time

#==============================================================================================

#Magnetic field Sweep 54K


drive tc1_driveable 100
wait 30
drive ma1_setpoint 0
wait 10
drive tc1_driveable 4
wait 30

drive tc1_driveable 53.5
wait 30


newfile HISTOGRAM_XY
drive ma1_setpoint 0
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 25
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 50
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 75
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 100
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 125
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 150
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 175
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 200
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 225
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 250
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 275
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 300
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 325
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 350
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 375
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 400
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 425
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 450
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 475
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 500
histmem start block
save
histmem stop

drive tc1_driveable 100

