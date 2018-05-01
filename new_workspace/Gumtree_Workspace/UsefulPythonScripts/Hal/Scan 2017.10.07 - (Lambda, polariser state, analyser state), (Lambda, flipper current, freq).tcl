#drive srce 180

proc scanAnalyser { } {
	set preset 180
	gumput scanAnalyser: Count Analyser +
	he3 analyser/spin 1
	wait 3
	runscan dummy_motor 0 1 1 time $preset datatype HISTOGRAM_XY
	gumput scanAnalyser: Count Analyser -
	he3 analyser/spin -1
	wait 3
	runscan dummy_motor 0 1 1 time $preset datatype HISTOGRAM_XY

}

proc scanSpinState { } {
	set preset 120
	
	# configuration unpol 1
	gumput scanSpinState: Unpol 1
	#driveGuide(guideConfig.g1)
	::optics::guide g1
	#don't change below scan command
	gumput scanSpinState: Count
	runscan dummy_motor 0 1 1 time $preset datatype HISTOGRAM_XY

	
	# configuration polariser -
	#polariser in
	gumput scanSpinState: Polariser + SF on
	::optics::guide p1
	hset /instrument/flipper/set_flip_on 1
	wait 60
	scanAnalyser
	
	# configuration polariser +
	# Drive flipper
	gumput scanSpinState: Polariser + SF off
	hset /instrument/flipper/set_flip_on 0
	wait 3
	scanAnalyser
}

proc scanSpinStateFreq { } {
	set freqList {260 262 264 265 266 267 268 269 270 272 274}
	for {set j 0} {$j < [llength $freqList]} { incr j} {
		gumput scanFreq: Flipper Freq = [lindex $freqList $j]
		hset /instrument/flipper/set_frequency [lindex $freqList $j]
		wait 3
		scanSpinState	
	}
}


proc scanSpinStateFreqLambda { } {
	set lbdList {5.76 7.0 8.0}
	set attList {180 150 120}
	for {set i 0} {$i < [llength $lbdList]} { incr i} {
		drive att 270
		drive nvs_lambda [lindex $lbdList $i]
		drive att [lindex $attList $i]
		gumput scanSpinStateLambda: Lambda=[lindex $lbdList $i] Att=[lindex $attList $i]
		scanSpinStateFreq
	}
}

#hset /instrument/flipper/set_current 7.1
#wait 60
#hset /instrument/flipper/set_frequency 385
#wait 5
#hset /instrument/flipper/set_flip_on 0
#wait 5

scanSpinStateFreqLambda

gumput experiment finished