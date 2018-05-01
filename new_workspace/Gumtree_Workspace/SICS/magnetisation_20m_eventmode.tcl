
oxfordsetrate 0.25
drive att 0
newfile HISTOGRAM_XY
histmem mode unlimited
oxfordseths on
histmem start
wait 35
oxfordsetfield 10.0
#0T to 10T in 2400s
wait 2460
oxfordsetfield -10.0
wait 4860
oxfordsetfield 10.0
wait 4860
oxfordsetfield 0.0
wait 2460
oxfordseths off
wait 35
save
histmem stop
######MEASURE SCATTERING AT 10T for 20m######
# Move the beamstop out
#driveBsx(17, 100)
drive bsx 18
#driveAtt(300)
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 900
histmem start block
save
######MEASURE TRANSMISSION AT 10T for 20m######
drive att 330
# Move the beamstop out
#driveBsx(17, 100)
drive bsx 118
#driveAtt(300)
drive att 240
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
######end######