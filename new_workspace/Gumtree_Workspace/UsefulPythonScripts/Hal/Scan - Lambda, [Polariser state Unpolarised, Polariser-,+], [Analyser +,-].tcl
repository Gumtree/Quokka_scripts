drive srce 180

proc scanAnalyser { } {
	set preset 22500000
	gumput scanAnalyser: Count Analyser + $preset
	runscan dummy_motor 0 1 1 MONITOR_1 $preset datatype HISTOGRAM_XY
	hset /sample/isops/relay 1
	wait 3
	hset /sample/isops/relay 0
	gumput scanAnalyser: Count Analyser - $preset
	runscan dummy_motor 0 1 1 MONITOR_1 $preset datatype HISTOGRAM_XY
	hset /sample/isops/relay 1
	wait 3
	hset /sample/isops/relay 0

}

proc scanSpinState { } {
	set preset 22500000
	
	# configuration unpol 1
	gumput scanSpinState: Unpol 1
	#driveGuide(guideConfig.g1)
	::optics::guide g1
	#don't change below scan command
	gumput scanSpinState: Count $preset
	runscan dummy_motor 0 1 1 MONITOR_1 $preset datatype HISTOGRAM_XY

	
	# configuration polariser -
	#polariser in
	gumput scanSpinState: Polariser -
	::optics::guide p1
	scanAnalyser
	
	# configuration polariser +
	# Drive flipper
	gumput scanSpinState: Polariser +
	hset /instrument/flipper/set_flip_on 1
	wait 60
	scanAnalyser
	
	# configuration unpol 2
	#polariser out
	gumput scanSpinState: Unpol 2
	hset /instrument/flipper/set_flip_on 0
	wait 3
	::optics::guide g1
	gumput scanSpinState: Count $preset
	runscan dummy_motor 0 1 1 MONITOR_1 $preset datatype HISTOGRAM_XY
}

proc scanSpinStateLambda { } {
	set lbdList {5.76 4.502 7.0}
	set attList {270 300 240}
	for {set i 0} {$i < [llength $lbdList]} { incr i} {
		drive nvs_lambda [lindex $lbdList $i]
		drive att [lindex $attList $i]
		gumput scanSpinStateLambda: Lambda=[lindex $lbdList $i] Att=[lindex $attList $i]
		scanSpinState
	}
}

hset /instrument/flipper/set_current 7.1
wait 60
hset /instrument/flipper/set_frequency 407
wait 30
hset /instrument/flipper/set_flip_on 0
wait 3

scanSpinStateLambda

gumput experiment finished