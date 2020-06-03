histmem preset 180
histmem mode time


#H-T Phase Diagram
#temperature sweep at 700 Oe from 12K 

#drive tc1_driveable 12
#wait 10
#drive ma1_setpoint 700
#wait 10

newfile HISTOGRAM_XY
#drive tc1_driveable 12
histmem start block
save
histmem stop
