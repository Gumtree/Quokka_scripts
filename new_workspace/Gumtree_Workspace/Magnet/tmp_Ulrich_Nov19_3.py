histmem preset 30
histmem mode time

#======================================================================

#temperature sweep at 350 Oe from 4K 

newfile HISTOGRAM_XY
drive samphi -2
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive samphi -1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive samphi 0
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive samphi 1
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
drive samphi 2
histmem start block
save
histmem stop

