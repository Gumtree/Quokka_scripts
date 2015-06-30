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

drive att 300
drive bsx 144
drive att 150
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
histmem preset 10
histmem start block
save
#
######TRANS######
drive att 330
drive bsx 144
drive att 150
newfile HISTOGRAM_XY
histmem mode time
histmem preset 10
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
histmem preset 10
histmem start block
save
#
######TRANS######
drive att 330
drive bsx 144
drive att 150
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
######TRANS######
drive att 330
drive bsx 144
drive att 150
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
######TRANS######
drive att 330
drive bsx 144
drive att 150
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
######TRANS######
drive att 330
drive bsx 144
drive att 150
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
######TRANS######
drive att 330
drive bsx 144
drive att 150
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
######TRANS######
drive att 330
drive bsx 144
drive att 150
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
######TRANS######
drive att 330
drive bsx 144
drive att 150
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
######TRANS######
drive att 330
drive bsx 144
drive att 150
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
######TRANS######
drive att 330
drive bsx 144
drive att 150
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
######TRANS######
drive att 330
drive bsx 144
drive att 150
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
######TRANS######
drive att 330
drive bsx 144
drive att 150
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
######TRANS######
drive att 330
drive bsx 144
drive att 150
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
######TRANS######
drive att 330
drive bsx 144
drive att 150
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
######TRANS######
drive att 330
drive bsx 144
drive att 150
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
######TRANS######
drive att 330
drive bsx 144
drive att 150
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
######TRANS######
drive att 330
drive bsx 144
drive att 150
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
######TRANS######
drive att 330
drive bsx 144
drive att 150
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