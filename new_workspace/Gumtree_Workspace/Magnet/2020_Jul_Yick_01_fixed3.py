histmem preset 60
histmem mode time


#After 300 K reset
#-----------------------------------------------------------------
#temperature sweep at 200 Oe from 4K 

newfile HISTOGRAM_XY
drive tc1_driveable 50
histmem start block
save
histmem stop


