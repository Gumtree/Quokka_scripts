histmem preset 120
histmem mode time

# drive tc1_driveable 60
# drive ma1_magnet_setpoint 0
# wait 60

drive tc1_driveable 56.5

newfile HISTOGRAM_XY
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0025
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0050
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0075
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0100
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0125
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0150
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0175
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0200
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0225
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0250
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0275
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0300
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0325
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0350
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0375
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0400
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0425
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0450
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0475
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0500
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0525
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0550
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0575
wait 60
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0600
wait 60
histmem start block
save
histmem stop


