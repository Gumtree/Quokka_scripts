drive srce 180

proc scanAnalyser { } {
	set preset 7500000
	gumput scanAnalyser: Count Analyser +
	runscan dummy_motor 0 1 1 MONITOR_1 $preset datatype HISTOGRAM_XY
	hset /sample/isops/relay 1
	wait 3
	hset /sample/isops/relay 0
	gumput scanAnalyser: Count Analyser -
	runscan dummy_motor 0 1 1 MONITOR_1 $preset datatype HISTOGRAM_XY
	hset /sample/isops/relay 1
	wait 3
	hset /sample/isops/relay 0

}

proc scanFreq { } {
	set freqList {377 387 397 407 417 427 437}
	for {set j 0} {$j < [llength $freqList]} { incr j} {
		gumput scanFreq: Flipper Freq = [lindex $freqList $j]
		hset /instrument/flipper/set_frequency [lindex $freqList $j]
		wait 3
		scanAnalyser	
	}
}

proc scanCurrent { } {
	set currentList {4.0 4.5 5.0 5.5 6.0 6.5 7.0 7.1}
	for {set k 0} {$k < [llength $currentList]} { incr k} {
		gumput scanCurrent: Flipper Current = [lindex $currentList $k]
		hset /instrument/flipper/set_current [lindex $currentList $k]
		wait 60
		scanFreq
	}
}

proc scanFreqCurrentLambda { } {
	set lbdList {5.76 4.502 7.0}
	set attList {270 300 240}
	
	#polariser in
	gumput scanFreqCurrentLambda: Polariser in
	::optics::guide p1
	
	for {set i 0} {$i < [llength $lbdList]} { incr i} {
		drive nvs_lambda [lindex $lbdList $i]
		drive att [lindex $attList $i]
		gumput scanFreqCurrentLambda: Lambda=[lindex $lbdList $i] Att=[lindex $attList $i]
		scanCurrent
	}
}

proc scanSpinState { } {
	set preset 7500000
	
	# configuration unpol 1
	gumput scanSpinState: Unpol 1
	#driveGuide(guideConfig.g1)
	::optics::guide g1
	#don't change below scan command
	gumput scanSpinState: Count
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
	hset /instrument/flipper/set_current 7.1
	wait 60
	hset /instrument/flipper/set_frequency 397
	wait 5
	scanAnalyser
	
	# configuration unpol 2
	#polariser out
	gumput scanSpinState: Unpol 2
	hset /instrument/flipper/set_flip_on 0
	wait 3
	::optics::guide g1
	gumput scanSpinState: Count
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
hset /instrument/flipper/set_frequency 397
wait 5
hset /instrument/flipper/set_flip_on 0
wait 5

scanSpinStateLambda
scanFreqCurrentLambda

gumput experiment finished