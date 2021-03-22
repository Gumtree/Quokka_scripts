histmem preset 60
histmem mode time


#Time scan
#-----------------------------------------------------------------
#System reset (15 minutes)

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 0
drive tc1_driveable 120
wait 10

drive tc1_driveable 4
drive ma1_setpoint 200
# wait 10

drive tc1_driveable 10
wait 300

drive tc1_driveable 20
wait 300

drive tc1_driveable 30
wait 300

drive tc1_driveable 40
wait 300

drive tc1_driveable 50
wait 300

hset /sample/tc1/control/tolerance1 0.1

drive tc1_driveable 51

drive tc1_driveable 53

drive tc1_driveable 55

drive tc1_driveable 56.1
wait 10

#-----------------------------------------------------------------

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

