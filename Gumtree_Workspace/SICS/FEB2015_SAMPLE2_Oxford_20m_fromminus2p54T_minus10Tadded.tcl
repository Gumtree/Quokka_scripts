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
#DRIVE -5T to -10T
#drive from -5T to -8T @ 0.2T/min = 15 minutes
oxfordsetrate 0.2
oxfordseths on
wait 35
oxfordsetfield -8.0
wait 960
#drive from -8T to -10T @ 0.1T/min = 20 minutes
oxfordsetrate 0.1
#oxfordseths on
#wait 35
oxfordsetfield -10.0
wait 1260
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
histmem preset 5400
histmem start block
save
#
#drive from -10T to -8T @ 0.1T/min = 20 minutes
oxfordsetrate 0.1
oxfordseths on
wait 35
oxfordsetfield -8.0
wait 1260
#oxfordseths off
#drive from -8T to -5T @ 0.2T/min = 15 minutes
oxfordsetrate 0.2
#oxfordseths on
#wait 35
oxfordsetfield -5.0
wait 960
#DRIVE -5.0T to 0.0T (10 minutes)
oxfordsetrate 0.5
#oxfordseths on
#wait 35
oxfordsetfield 0
wait 660
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
#
#no need to wait when running transmission#
#wait 35
#now collect data at this field
######EXTRA_DATA_AT_0T######
#newfile HISTOGRAM_XY
#histmem mode unlimited
#histmem start
######press save as end of run######