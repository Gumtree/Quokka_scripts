
histmem mode time

run att 90
reldrive bsx 100
histmem preset 120
newfile HISTOGRAM_XY
histmem start
save
histmem stop
reldrive bsx -100
run att 0
