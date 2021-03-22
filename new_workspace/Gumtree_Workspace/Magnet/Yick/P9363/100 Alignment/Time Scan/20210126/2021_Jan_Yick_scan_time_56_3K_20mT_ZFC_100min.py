histmem preset 60
histmem mode time


#Time scan
#-----------------------------------------------------------------
#System reset (15 minutes)

hset /sample/tc1/control/tolerance1 1

drive ma1_setpoint 200
drive tc1_driveable 120
wait 10

drive tc1_driveable 4
wait 10

hset /sample/tc1/control/tolerance1 0.2

drive tc1_driveable 50

drive tc1_driveable 52

drive tc1_driveable 53

drive tc1_driveable 54

drive tc1_driveable 55

drive tc1_driveable 56

drive tc1_driveable 56.3
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

# 70 minutes

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

# 80 minutes

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

# 90 minutes

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

# 100 minutes