#Reset to 200K with magnetic oscillation for sample transfer
hset /sample/ma1/magnet/pressure_setpoint 3

drive ma1_magnet_setpoint 0.04

drive ma1_magnet_setpoint -0.04

drive ma1_magnet_setpoint 0.02

drive ma1_magnet_setpoint -0.02

drive ma1_magnet_setpoint 0.010

drive ma1_magnet_setpoint -0.01

drive ma1_magnet_setpoint 0.005

drive ma1_magnet_setpoint -0.005

drive ma1_magnet_setpoint 0
wait 30