#Measure a transmission
run att 150
wait 20
drive bsx 138
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
histmem stop
drive bsx 38
run att 0
wait 20