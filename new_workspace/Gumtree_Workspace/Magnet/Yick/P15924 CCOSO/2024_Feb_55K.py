histmem preset 60
histmem mode time

newfile HISTOGRAM_XY
drive tc1_driveable 55
drive tc1_driveable2 55
wait 10

histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop

newfile HISTOGRAM_XY
histmem start block
save
histmem stop