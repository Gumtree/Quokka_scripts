#SCRIPT NEEDS TO BE CHECKED
#CHECK ATT MOVED TO 300 PRIOR TO MOVING BEAMSTOP FOR TRANSMISSION - EPG 11/02/15

######SET-UP FOR 20m
drive att 330
###### Feb2015 ######
drive srce 30
# Drive guide to ga
#driveGuide(guideConfig.ga)
::optics::guide lens
#selBs(2)
# set beamcentres
#sics.set('beamcenterx', 93.9172)
beamcenterx 94.3798
#sics.set('beamcenterz', 96.9296)
beamcenterz 94.1367
drive bsz 244
#
###ALREADY COLLECTED TRANSMISSION FOR THIS SAMPLE###
######TRANS######
#drive bsx 194
#drive att 90
#newfile HISTOGRAM_XY
#histmem mode time
#histmem preset 120
#histmem start block
#save
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
#NOT COLLECTING DATA AT 0T FOR THIS SAMPLE#
#RAMPING DIRECTLY TO 10T#
#drive att 0
#newfile HISTOGRAM_XY
#histmem mode count
#histmem preset 2.0e6
#histmem start block
#save
#
#
#DRIVE 0T to 10T
#drive from 0T to 5T @ 0.5T/min = 10 minutes
#drive from 5T to 8T @ 0.2T/min = 15 minutes
#drive from 8T to 10T @ 0.1T/min = 20 minutes
#collect data during field change
#data file length depends on ramp rate
drive att 0
newfile HISTOGRAM_XY
histmem mode unlimited
oxfordsetrate 0.5
oxfordseths on
wait 35
histmem start
oxfordsetfield 5.0
wait 600
#drive from 5T to 8T @ 0.2T/min = 15 minutes
oxfordsetrate 0.2
#oxfordseths on
#wait 35
oxfordsetfield 8.0
wait 900
#drive from 8T to 10T @ 0.1T/min = 20 minutes
oxfordsetrate 0.1
#oxfordseths on
#wait 35
oxfordsetfield 10.0
wait 1200
oxfordseths off
save
histmem stop
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######TRANS######
drive bsx 194
drive att 90
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode count
histmem preset 2.0e6
histmem start block
save
#
#
#DRIVE 10T to 5T
#drive 10T to 8T @ 0.1T/min = 20 minutes
oxfordsetrate 0.1
oxfordseths on
wait 35
oxfordsetfield 8.0
wait 1200
#drive from 8T to 5T @ 0.2T/min = 15 minutes
oxfordsetrate 0.2
#oxfordseths on
#wait 35
oxfordsetfield 5.0
wait 900
oxfordseths off
#
######TRANS######
drive bsx 194
drive att 90
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode count
histmem preset 2.0e6
histmem start block
save
#
#
#DRIVE 5T to 0T @ 0.5T/min (10 min)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 0
wait 600
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######TRANS######
drive bsx 194
drive att 90
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode count
histmem preset 2.0e6
histmem start block
save
#
#
#DRIVE 0T to -1.15T (3 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -1.15
wait 180
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######TRANS######
drive bsx 194
drive att 90
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode count
histmem preset 2.0e6
histmem start block
save
#
#
#DRIVE -1.15T to -1.25T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -1.25
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######TRANS######
drive bsx 194
drive att 90
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode count
histmem preset 2.0e6
histmem start block
save
#
#
#DRIVE -1.25T to -1.35T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -1.35
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######TRANS######
drive bsx 194
drive att 90
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode count
histmem preset 2.0e6
histmem start block
save
#
#
#DRIVE -1.35T to -1.45T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -1.45
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######TRANS######
drive bsx 194
drive att 90
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode count
histmem preset 2.0e6
histmem start block
save
#
#
#DRIVE -1.45T to -1.55T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -1.55
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######TRANS######
drive bsx 194
drive att 90
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode count
histmem preset 2.0e6
histmem start block
save
#
#
#DRIVE -1.55T to -1.65T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -1.65
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######TRANS######
drive bsx 194
drive att 90
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode count
histmem preset 2.0e6
histmem start block
save
#
#
#DRIVE -1.65T to -1.75T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -1.75
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######TRANS######
drive bsx 194
drive att 90
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode count
histmem preset 2.0e6
histmem start block
save
#
#
#DRIVE -1.75T to -5.0T (6.5 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -5.0
wait 420
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######TRANS######
drive bsx 194
drive att 90
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode count
histmem preset 2.0e6
histmem start block
save
#
#
#DRIVE -5.0T to -10.0T
#drive -5T to -8T @ 0.2T/min = 15 minutes
oxfordsetrate 0.2
oxfordseths on
wait 35
oxfordsetfield -8.0
wait 900
#drive from -8T to -10T @ 0.1T/min = 20 minutes
oxfordsetrate 0.1
#oxfordseths on
#wait 35
oxfordsetfield -10.0
wait 1200
oxfordseths off
#
######TRANS######
drive bsx 194
drive att 90
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode count
histmem preset 2.0e6
histmem start block
save
#
#
#DRIVE -10.0T to 0.0T (6.5 minutes)
#drive -10T to -8T @ 0.1T/min = 20 minutes
oxfordsetrate 0.1
oxfordseths on
wait 35
oxfordsetfield -8.0
wait 1200
#drive from -8T to -5T @ 0.2T/min = 15 minutes
oxfordsetrate 0.2
#oxfordseths on
#wait 35
oxfordsetfield -5.0
wait 900
#drive from -5T to -0T @ 0.5T/min = 10 minutes
oxfordsetrate 0.5
#oxfordseths on
#wait 35
oxfordsetfield 0.0
wait 600
oxfordseths off
#
######TRANS######
drive bsx 194
drive att 90
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode count
histmem preset 2.0e6
histmem start block
save
#
#
#no need to wait when running transmission#
#wait 35
#now collect data at this field
######EXTRA_DATA_AT_0T######
#newfile HISTOGRAM_XY
#histmem mode unlimited
#histmem start
######press save as end of run######