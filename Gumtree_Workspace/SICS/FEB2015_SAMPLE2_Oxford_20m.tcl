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
histmem preset 1800
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
histmem preset 1800
histmem start block
save
#
#
#DRIVE 0.2T to 1T (2 mins)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 1.0
wait 180
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
histmem preset 1800
histmem start block
save
#
#
#DRIVE 1T to 2T (4 min)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 2.0
wait 300
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
histmem preset 1800
histmem start block
save
#
#DRIVE 2T to 2.4T (1 min)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 2.4
wait 120
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
histmem preset 1800
histmem start block
save
#
#DRIVE 2.4T to 10T
#drive from 2.4T to 5T @ 0.5T/min = 5 minutes
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield 5.0
wait 360
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
histmem preset 5400
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
histmem preset 1800
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
histmem preset 1800
histmem start block
save
#
#
#DRIVE 0T to -1.84T (4 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -1.84
wait 300
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
histmem preset 1800
histmem start block
save
#
#
#DRIVE -1.84T to -1.94T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -1.94
wait 60
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
histmem preset 1800
histmem start block
save
#
#
#DRIVE -1.94T to -2.04T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.04
wait 60
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
histmem preset 1800
histmem start block
save
#
#
#DRIVE -2.04T to -2.14T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.14
wait 60
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
histmem preset 1800
histmem start block
save
#
#
#DRIVE -2.14T to -2.24T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.24
wait 60
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
histmem preset 1800
histmem start block
save
#
#
#DRIVE -2.24T to -2.34T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.34
wait 60
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
histmem preset 1800
histmem start block
save
#
#
#DRIVE -2.34T to -2.44T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.44
wait 60
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
histmem preset 1800
histmem start block
save
#
#
#DRIVE -2.44T to -5.0T (5 minutes)
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
histmem preset 1800
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