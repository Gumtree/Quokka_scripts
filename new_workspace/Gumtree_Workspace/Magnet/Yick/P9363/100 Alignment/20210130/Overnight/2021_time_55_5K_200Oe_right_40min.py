histmem preset 60
histmem mode time


#Time scan
#-----------------------------------------------------------------
#System reset (15 minutes)

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 90
wait 10
drive ma1_setpoint 200
wait 10
hset /sample/tc1/control/tolerance1 0.2
drive tc1_driveable 55.8
#-----------------------------------------------------------------

drive ma1_setpoint 200

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

# 10 minutes

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

# 20 minutes

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

# 30 minutes

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

# 40 minutes

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

# 50 minutes

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

# 60 minutes
