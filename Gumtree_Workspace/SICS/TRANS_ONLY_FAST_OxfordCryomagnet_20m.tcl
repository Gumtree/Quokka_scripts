######TRANSMISSION ONLY SCRIPT######
######SET-UP FOR 20m
drive att 330
drive srce 60
# Drive guide to ga
#driveGuide(guideConfig.ga)
::optics::guide ga
# Drive entrance aperture to 180 (for guide g6)
# Drive beamstops up
#selBs(1)
# set beamcentres
#sics.set('beamcenterx', 93.9172)
beamcenterx 93.6977
#sics.set('beamcenterz', 96.9296)
beamcenterz 95.4997
######MEASURE TRANSMISSION AT 10T for 20m######
# Move the beamstop out
#driveBsx(17, 100)
drive bsx 115
#driveAtt(300)
drive att 240
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
############
#starting data collection @0T
#oxfordsetfield 10.0
#newfile HISTOGRAM_XY
#histmem mode time
#histmem preset 3600
#histmem start block
#save
#go to next field
#collect data during field change
#data file length depends on ramp rate
drive bsx 15
#driveBsz(262.5)
drive bsz 255
oxfordsetrate 0.5
drive att 0
newfile HISTOGRAM_XY
histmem mode unlimited
oxfordseths on
wait 35
histmem start
oxfordsetrate 0.5
oxfordsetfield 10.0
#0T to 10T in 1200s
wait 1260
oxfordseths off
wait 35
save
histmem stop
######MEASURE TRANSMISSION AT 10T for 20m######
drive att 330
# Move the beamstop out
#driveBsx(17, 100)
drive bsx 115
#driveAtt(300)
drive att 240
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#10T to 8T in 4 mins = 240s
oxfordseths on
wait 35
oxfordsetfield 8.0
wait 300
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#8T to 6T in 4 mins = 240s
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 6.0
wait 300
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#6T to 4T in 4 mins = 240s
oxfordseths on
wait 35
oxfordsetfield 4.0
wait 300
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#4T to 2T in 4 mins = 240s
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 2.0
wait 300
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#2T to 1T in 2 mins = 120s
oxfordseths on
wait 35
oxfordsetfield 1.0
wait 180
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#1T to 0.5T in 1 mins = 60s
oxfordseths on
wait 35
oxfordsetfield 0.5
wait 120
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#0.5T to 0.25T in 30s
oxfordseths on
wait 35
oxfordsetfield 0.25
wait 60
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#0.25T to 0T in 30s
oxfordseths on
wait 35
oxfordsetfield 0.0
wait 60
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#0T to -0.25T in 30s
oxfordseths on
wait 35
oxfordsetfield -0.25
wait 60
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#-0.25T to -0.5T in 30s
oxfordseths on
wait 35
oxfordsetfield -0.5
wait 60
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#-0.5T to -1.0T in 60s
oxfordseths on
wait 35
oxfordsetfield -1.0
wait 120
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#-1.0T to -1.1T in 30s
oxfordseths on
wait 35
oxfordsetfield -1.1
wait 60
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#-1.1T to -1.2T in 30s
oxfordseths on
wait 35
oxfordsetfield -1.2
wait 60
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#-1.2T to -1.3T in 30s
oxfordseths on
wait 35
oxfordsetfield -1.3
wait 60
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#-1.3T to -1.4T in 30s
oxfordseths on
wait 35
oxfordsetfield -1.4
wait 60
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#-1.4T to -1.5T in 30s
oxfordseths on
wait 35
oxfordsetfield -1.5
wait 60
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#-1.5T to -2.0T in 60s
oxfordseths on
wait 35
oxfordsetfield -2.0
wait 120
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#-2.0T to -4.0T in 240s
oxfordseths on
wait 35
oxfordsetfield -4.0
wait 300
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#-4.0T to -6.0T in 240s
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -6.0
wait 300
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#-6.0T to -8.0T in 240s
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -8.0
wait 300
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
#-8.0T to -10.0T in 4 mins = 240s
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -10.0
wait 300
oxfordseths off
wait 35
#now collect data at this field
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
drive att 330
######
######SCATTERING SET-UP FOR 20m######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
#driveBsx(17, 0)
drive bsx 15
#driveBsz(262.5)
drive bsz 255
############
#starting data collection @-10T to 0T
#oxfordsetfield 10.0
#newfile HISTOGRAM_XY
#histmem mode time
#histmem preset 3600
#histmem start block
#save
#go to next field
#collect data during field change
#data file length depends on ramp rate
oxfordsetrate 0.5
drive att 0
newfile HISTOGRAM_XY
histmem mode unlimited
oxfordseths on
wait 35
histmem start
oxfordsetfield 0.0
#-10T to 0T in 1200s
wait 1260
oxfordseths off
wait 35
save
histmem stop
######MEASURE TRANSMISSION AT 0T for 20m######
drive att 330
# Move the beamstop out
#driveBsx(17, 100)
drive bsx 115
#driveAtt(300)
drive att 240
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
######end######