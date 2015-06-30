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
#DRIVE 0T to -1.64T (3 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -1.64
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
#DRIVE -1.64T to -1.74T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -1.74
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
#DRIVE -1.74T to -1.84T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -1.84
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
#DRIVE -2.44T to -2.54T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.54
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
#DRIVE -2.54T to -2.64T (1 minutes)
oxfordsetrate 0.5
oxfordseths on
wait 35
oxfordsetfield -2.64
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
#DRIVE -2.64T to -5.0T (5 minutes)
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