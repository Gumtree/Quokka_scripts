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
#DRIVE 0T to -2.07T (4 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.07
wait 300
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
#DRIVE -2.07T to -2.17T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.17
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
#DRIVE -2.17T to -2.27T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.27
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
#DRIVE -2.27T to -2.37T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.37
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
#DRIVE -2.37T to -2.47T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.47
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
#DRIVE -2.47T to -2.57T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.57
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
#DRIVE -2.57T to -2.67T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.67
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
#DRIVE -2.67T to -2.77T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.77
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
#DRIVE -2.77T to -2.87T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.87
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
#DRIVE -2.87T to -2.97T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.97
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
#DRIVE -2.97T to -3.07T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -3.07
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
#DRIVE -3.07T to -5.0T (4 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -5.0
wait 300
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