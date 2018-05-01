###SCRIPT FOR RUNNING FRESH SAMPLE AND COLLECTING AT 0T AT START###
######SET-UP FOR 20m
drive att 330
drive srce 150
# Drive guide to ga
#driveGuide(guideConfig.ga)
::optics::guide ga
#selBs(2)
beamcenterx 95.0494
beamcenterz 94.1318
drive bsz 249
######IF ALREADY AT 20M THEN NEXT LINES COMMENTED OUT######
######START OF COMMENTED LINES######
#dhv1 down
#wait 180
#drive det 19250
#dhv1 up
#wait 180
######END OF COMMENTED LINES OUT######
######TRANS######
drive att 330
drive bsx 151
drive att 210
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
######SCATTERING @ 0T######
# Drive attenuator to safe value
drive att 330
# Move the beamstop in
drive bsx 51
############
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 600
histmem start block
save
#
######DRIVE 0T to 10T EVENT MODE IN SCATTERING SET-UP######
newfile HISTOGRAM_XY
histmem mode unlimited
histmem start
hset /sample/ma1/magnet/rate 0.1
drive ma1_magnet_setpoint 10
#wait 20 mins for ramp plus 35 plus 60
save
histmem stop
######SCATTERING @ 10T######
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 600
histmem start block
save
######TRANSMISSION @ 10T######
drive att 330
drive bsx 151
drive att 210
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
######DRIVE 10T to 0T EVENT MODE IN SCATTERING SET-UP######
drive att 330
drive bsx 51
drive att 0
newfile HISTOGRAM_XY
histmem mode unlimited
histmem start
hset /sample/ma1/magnet/rate 0.1
drive ma1_magnet_setpoint 0
#wait 100 mins for ramp plus 35 plus 60
save
histmem stop
######SCATTERING @ 0T######
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 600
histmem start block
save
######TRANSMISSION @ 0T######
drive att 330
drive bsx 151
drive att 210
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
drive att 330
######DRIVE 0T to -10T EVENT MODE IN SCATTERING SET-UP######
drive att 330
drive bsx 51
drive att 0
newfile HISTOGRAM_XY
histmem mode unlimited
histmem start
hset /sample/ma1/magnet/rate 0.1
drive ma1_magnet_setpoint -10
#wait 100 mins for ramp plus 35 plus 60
save
histmem stop
######TRANSMISSION @- 10T######
drive att 330
drive bsx 151
drive att 210
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
drive att 330
######SCATTERING @ -10T######
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 600
histmem start block
save
######DRIVE -10T to 0T EVENT MODE IN SCATTERING SET-UP######
drive att 330
drive bsx 51
drive att 0
newfile HISTOGRAM_XY
histmem mode unlimited
histmem start
hset /sample/ma1/magnet/rate 0.1
drive ma1_magnet_setpoint 0
#wait 100 mins for ramp plus 35 plus 60
save
histmem stop
######SCATTERING @ 0T######
drive att 0
newfile HISTOGRAM_XY
histmem mode time
histmem preset 600
histmem start block
save
######TRANSMISSION @ 0T######
drive att 330
drive bsx 151
drive att 210
newfile HISTOGRAM_XY
histmem mode time
histmem preset 120
histmem start block
save
drive att 330
