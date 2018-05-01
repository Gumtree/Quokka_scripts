drive srce 180

proc scanLambda { } {
	set lbdList {5.76 4.502}
	set attList {300 270}
	set preset 75000
	
	for {set i 0} {$i < [llength $lbdList]} { incr i} {
		drive nvs_lambda [lindex $lbdList $i]
		drive att [lindex $attList 0]
		runscan dummy_motor 0 1 1 MONITOR_1 $preset datatype HISTOGRAM_XY
	}
}

# configuration unpol 1
gumput drive to configuration unpol 1
#driveGuide(guideConfig.g1)
::optics::guide g1
#don't change below scan command
scanLambda

# configuration -+
#polariser in
gumput drive to configuration -+
::optics::guide p1
scanLambda
#
# configuration --
#polariser in
gumput drive to configuration --
hset /sample/isops/relay 1
wait 3
hset /sample/isops/relay 0
scanLambda

#
# configuration +-
# Drive flipper
gumput drive to configuration +-
hset /instrument/flipper/set_flip_on 1
#sics.set('/instrument/flipper/set_frequency', 407)
wait 60
scanLambda

#
# configuration ++
# Drive flipper
gumput drive to configuration ++
hset /sample/isops/relay 1
wait 3
hset /sample/isops/relay 0
scanLambda

# configuration unpol2
#polariser out
gumput drive to configuration unpol 2
hset /instrument/flipper/set_flip_on 0
wait 3
::optics::guide g1
scanLambda

gumput experiment finished