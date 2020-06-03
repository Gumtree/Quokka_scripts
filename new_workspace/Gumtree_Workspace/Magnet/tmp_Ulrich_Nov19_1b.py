histmem preset 60
histmem mode time

#==============================================================================================
#

drive tc1_driveable 80
wait 10
drive ma1_setpoint 0
wait 10
drive tc1_driveable 4
wait 10
drive tc1_driveable 4
wait 10


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

newfile HISTOGRAM_XY
drive ma1_setpoint 525
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 550
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 575
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 600
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 625
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 650
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 675
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 700
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 725
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 750
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 775
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 800
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 825
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 850
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 875
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 900
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 925
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 950
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 975
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_setpoint 1000
histmem start block
save
histmem stop

drive tc1_driveable 100