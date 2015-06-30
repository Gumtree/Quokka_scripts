###SCRIPT FOR RUNNING FRESH SAMPLE AND COLLECTING AT 0T AT START###

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
beamcenterx 94.6116
#sics.set('beamcenterz', 96.9296)
beamcenterz 92.5075
drive bsz 244

######TRANS######
drive att 330
drive bsx 144
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
histmem mode time
histmem preset 600
histmem start block
save
#
#DRIVE 0T to 0.2T
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 0.2
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 600
histmem start block
save
#
#
#DRIVE 0.2T to 0.4T
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 0.4
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 600
histmem start block
save
#
#
#DRIVE 0.4T to 0.6T
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 0.6
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 600
histmem start block
save
#
#
#DRIVE 0.6T to 0.8T
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 0.8
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 600
histmem start block
save
#
#
#DRIVE 0.8T to 1T
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 1.0
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 600
histmem start block
save
#
#
#DRIVE 1T to 1.2T
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 1.2
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 600
histmem start block
save
#
#
#DRIVE 1.2T to 1.4T
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 1.4
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 600
histmem start block
save
#
#
#DRIVE 1.4T to 1.6T
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 1.6
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 600
histmem start block
save
#
#
#DRIVE 1.6T to 1.8T
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 1.8
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 600
histmem start block
save
#
#
#DRIVE 1.8T to 2T
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 2.0
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 600
histmem start block
save
#
#
#DRIVE 2T to 2.2T
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 2.2
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 600
histmem start block
save
#
#
#DRIVE 2.2T to 2.4T
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 2.4
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 600
histmem start block
save
#
#
#DRIVE 2.4T to 2.6T
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 2.6
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 600
histmem start block
save
#
#
#DRIVE 2.6T to 2.8T
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 2.8
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 600
histmem start block
save
#
#
#DRIVE 2.8T to 3T
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 3.0
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 600
histmem start block
save
#
#DRIVE 3T to 10T
#drive from 3T to 5T @ 0.5T/min = 4 minutes
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 5.0
wait 300
#drive from 5T to 8T @ 0.2T/min = 15 minutes
oxfordsetrate 0.2
#oxfordseths on
#wait 35
oxfordsetfield 8.0
wait 960
#drive from 8T to 10T @ 0.1T/min = 20 minutes
oxfordsetrate 0.1
#oxfordseths on
#wait 35
oxfordsetfield 10.0
wait 1260
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######TRANS######
drive att 330
drive bsx 144
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
histmem mode time
histmem preset 2700
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
wait 1260
#drive from 8T to 5T @ 0.2T/min = 15 minutes
oxfordsetrate 0.2
#oxfordseths on
#wait 35
oxfordsetfield 5.0
wait 960
oxfordseths off
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 1200
histmem start block
save
#
#
#DRIVE 5T to 0T @ 0.5T/min (10 min)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 0
wait 660
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 1200
histmem start block
save
#
#
#DRIVE 0T to -1.53T (3 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -1.53
wait 240
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 1200
histmem start block
save
#
#
#DRIVE -1.53T to -1.63T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -1.63
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 1200
histmem start block
save
#
#DRIVE -1.63T to -1.73T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -1.73
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 1200
histmem start block
save
#
#
#DRIVE -1.73T to -1.83T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -1.83
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 1200
histmem start block
save
#
#
#DRIVE -1.83T to -1.93T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -1.93
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 1200
histmem start block
save
#
#
#DRIVE -1.93T to -2.03T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.03
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 1200
histmem start block
save
#
#
#DRIVE -2.03T to -2.13TT (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.13
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 1200
histmem start block
save
#
#
#DRIVE -2.13T to -2.23T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.23
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 1200
histmem start block
save
#
#
#DRIVE -2.23T to -2.33T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.33
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 1200
histmem start block
save
#
#
#DRIVE -2.33T to -2.43T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.43
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 1200
histmem start block
save
#
#
#DRIVE -2.43T to -2.53T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.53
wait 60
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 1200
histmem start block
save
#
#
#DRIVE -2.53T to -5.0T (5 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -5.0
wait 360
oxfordseths off
#no need to wait when running transmission#
#wait 35
#now collect data at this field
#
######SCATTERING######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 44
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 1200
histmem start block
save
#
#DRIVE -5.0T to 0.0T (10 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 0
wait 660
oxfordseths off
#
#no need to wait when running transmission#
#wait 35
#now collect data at this field
######EXTRA_DATA_AT_0T######
#newfile HISTOGRAM_XY
#histmem mode unlimited
#histmem start
######press save as end of run######