histmem preset 60
histmem mode time


#Time scan
#-----------------------------------------------------------------
#System reset (15 minutes) 

hset /sample/tc1/control/tolerance1 0.5

drive tc1_driveable 120
wait 10

drive ma1_setpoint 0
wait 10

drive tc1_driveable 4
wait 10

drive ma1_setpoint 200
wait 10

hset /sample/tc1/control/tolerance1 0.2

drive tc1_driveable 56
wait 10

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

# 110 minutes

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

# 120 minutes

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

# 130 minutes

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

# 140 minutes

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

# 150 minutes

# 100 minutes

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

# 110 minutes

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

# 120 minutes

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

# 130 minutes

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

# 140 minutes

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
