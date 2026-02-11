#ZFC_4K
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

histmem mode time
histmem preset 180

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

drive ma1_magnet_setpoint 0.01
wait 10
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

drive ma1_magnet_setpoint 0.02
wait 10
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

drive ma1_magnet_setpoint 0.03
wait 10
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

drive ma1_magnet_setpoint 0.04
wait 10
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

drive ma1_magnet_setpoint 0.05
wait 10
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

drive ma1_magnet_setpoint 0.075
wait 10
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

drive ma1_magnet_setpoint 0.1
wait 10
newfile HISTOGRAM_XY
histmem start block
save
histmem stop

#reset field and temperature
drive ma1_magnet_setpoint 0
wait 10
drive tc1_driveable2 120


