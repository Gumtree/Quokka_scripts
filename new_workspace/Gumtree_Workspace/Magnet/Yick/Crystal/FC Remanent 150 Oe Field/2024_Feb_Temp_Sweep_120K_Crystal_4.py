#120 K Background Scan

histmem mode time
histmem preset 600

newfile HISTOGRAM_XY
drive tc1_driveable 120
drive tc1_driveable2 120
wait 10
histmem start block
save
histmem stop