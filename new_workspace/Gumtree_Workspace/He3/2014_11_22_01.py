#assuming two sample positions
#samx = 40 is Ag behenate
#samx = 5 is paraffin
#current config is p5 (polarised)
#lambda = 8 A
#resolution = 10%
#collect scattering data on AgBe

run samx 40
he3 analyser/spin 1
wait 2
he3 analyser/spin 0
wait 2
newfile HISTOGRAM_XY
histmem mode time
histmem preset 900 
histmem start block
save
he3 analyser/spin 0
wait 2

he3 analyser/spin -1
wait 2
he3 analyser/spin 0
wait 2
newfile HISTOGRAM_XY
histmem mode time
histmem preset 900 
histmem start block
save
he3 analyser/spin 0
wait 2

run samx 5
he3 analyser/spin 1
wait 2
he3 analyser/spin 0
wait 2
newfile HISTOGRAM_XY
histmem mode time
histmem preset 900 
histmem start block
save
he3 analyser/spin 0
wait 2

he3 analyser/spin -1
wait 2
he3 analyser/spin 0
wait 2
newfile HISTOGRAM_XY
histmem mode time
histmem preset 900 
histmem start block
save
he3 analyser/spin 0
wait 2



#silver ????? 
#check spin status
he3 analyser/spin 0
