histmem preset 300
histmem mode time

run att 0

#-------
#hset /sample/ma1/magnet/pressure_setpoint 15
#wait 10

#paramagnetic reset
drive tc1_driveable2 65
wait 60

#magnet oscillation
#drive ma1_magnet_setpoint 0.1
#drive ma1_magnet_setpoint -0.05
drive ma1_magnet_setpoint 0.025
drive ma1_magnet_setpoint -0.01
drive ma1_magnet_setpoint 0.005
drive ma1_magnet_setpoint -0.002
drive ma1_magnet_setpoint 0

hset /sample/ma1/magnet/pressure_setpoint 10
wait 10
drive tc1_driveable2 57
wait 60
hset /sample/ma1/magnet/pressure_setpoint 3
wait 10

#ZFC 0 -> 50 -> 0
newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0025
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.005
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0075
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.01
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0125
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.015
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0175
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.02
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0225
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.025
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0275
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.03
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0325
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.035
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0375
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.04
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0425
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.045
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0475
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.05
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0475
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.045
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0425
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.04
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0375
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.035
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0325
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.03
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0275
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.025
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0225
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.02
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0175
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.015
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0125
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.01
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0075
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.005
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0025
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0
histmem start block
save
histmem stop

#paramagnetic reset
drive tc1_driveable2 65
wait 60

#magnet oscillation
drive ma1_magnet_setpoint 0.1
drive ma1_magnet_setpoint -0.05
drive ma1_magnet_setpoint 0.025
drive ma1_magnet_setpoint -0.01
drive ma1_magnet_setpoint 0.005
drive ma1_magnet_setpoint -0.002
drive ma1_magnet_setpoint 0

#transmission scan and paramagnetic scan
histmem preset 600

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0
histmem start block
save
histmem stop

run att 90
reldrive bsx 100
newfile HISTOGRAM_XY
histmem start block
save
histmem stop
reldrive bsx -100
run att 0

histmem preset 300

#cooling
hset /sample/ma1/magnet/pressure_setpoint 10
wait 10
drive tc1_driveable2 57
wait 60
hset /sample/ma1/magnet/pressure_setpoint 3
wait 10

#FC 20 -> 50 -> 0 -> -50
newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.02
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0225
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.025
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0275
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.03
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0325
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.035
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0375
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.04
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0425
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.045
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0475
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.05
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0475
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.045
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0425
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.04
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0375
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.035
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0325
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.03
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0275
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.025
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0225
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.02
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0175
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.015
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0125
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.01
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0075
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.005
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0025
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.0025
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.005
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.0075
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.01
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.0125
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.015
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.0175
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.02
histmem start block
save
histmem stop

#paramagnetic reset
drive tc1_driveable2 65
wait 60

#magnet oscillation
drive ma1_magnet_setpoint 0.1
drive ma1_magnet_setpoint -0.05
drive ma1_magnet_setpoint 0.025
drive ma1_magnet_setpoint -0.01
drive ma1_magnet_setpoint 0.005
drive ma1_magnet_setpoint -0.002
drive ma1_magnet_setpoint 0

#cooling
hset /sample/ma1/magnet/pressure_setpoint 10
wait 10
drive tc1_driveable2 4
wait 60
hset /sample/ma1/magnet/pressure_setpoint 3
wait 10

#FC 20 -> 0 -> -20
newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.02
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0175
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.015
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0125
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.01
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0075
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.005
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0.0025
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint 0
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.0025
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.005
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.0075
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.01
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.0125
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.015
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.0175
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.02
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.0225
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.025
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.0275
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.03
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.0325
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.035
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.0375
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.04
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.0425
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.045
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.0475
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive ma1_magnet_setpoint -0.05
histmem start block
save
histmem stop