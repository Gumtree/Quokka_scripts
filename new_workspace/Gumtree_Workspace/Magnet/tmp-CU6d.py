histmem preset 120
histmem mode time


#==================================================================================================
drive tc1_driveable 60
drive ma1_magnet_setpoint 0.0
drive tc1_driveable 46

newfile HISTOGRAM_XY
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
drive ma1_magnet_setpoint 0.0100
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
drive ma1_magnet_setpoint 0.0200
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
drive ma1_magnet_setpoint 0.0300
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
drive ma1_magnet_setpoint 0.0400
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

