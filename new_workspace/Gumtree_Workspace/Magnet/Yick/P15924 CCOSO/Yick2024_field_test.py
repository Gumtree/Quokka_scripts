run ma1_magnet_setpoint 0.18
wait 240
histmem mode time
histmem preset 30
newfile HISTOGRAM_XY
histmem start block
save
histmem stop