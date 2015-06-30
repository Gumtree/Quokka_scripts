#drive srce 180

proc scanAnalyser { } {
	set preset 3000000
	gumput scanAnalyser: Count Analyser +
	he3 analyser/spin 1
	wait 2
	he3 analyser/spin 0
	wait 2
	runscan dummy_motor 0 1 1 MONITOR_1 $preset datatype HISTOGRAM_XY
	gumput scanAnalyser: Count Analyser -
	he3 analyser/spin -1
	wait 2
	he3 analyser/spin 0
	wait 2
	runscan dummy_motor 0 1 1 MONITOR_1 $preset datatype HISTOGRAM_XY
}

proc scanFreq { } {
	set freqList {380 385 390 395 400 405 410 415 420 425 430 435 392 397 402 407}
	for {set j 0} {$j < [llength $freqList]} { incr j} {
		gumput scanFreq: Flipper Freq = [lindex $freqList $j]
		hset /instrument/flipper/set_frequency [lindex $freqList $j]
		wait 3
		scanAnalyser
		gumput scanFreq: Flipper off, measure, then flipper on
		hset /instrument/flipper/set_flip_on 0
		wait 60
		scanAnalyser
		hset /instrument/flipper/set_flip_on 1
		wait 60		
	}
}

proc scanCurrent { } {
	set currentList {7.1}
	for {set k 0} {$k < [llength $currentList]} { incr k} {
		gumput scanCurrent: Flipper Current = [lindex $currentList $k]
		hset /instrument/flipper/set_current [lindex $currentList $k]
		wait 60
		scanFreq
	}
}

proc scanFreqCurrentLambda { } {
	set lbdList {7.0 5.0}
	set attList {90 150}
	
	#polariser in
	gumput scanFreqCurrentLambda: Polariser in
	::optics::guide p1

	hset /instrument/flipper/set_flip_on 1
	wait 60
	
	for {set i 0} {$i < [llength $lbdList]} { incr i} {
		drive nvs_lambda [lindex $lbdList $i]
		drive att [lindex $attList $i]
		gumput scanFreqCurrentLambda: Lambda=[lindex $lbdList $i] Att=[lindex $attList $i]
		scanCurrent
	}
}

proc scanSpinState { } {
	set preset 3000000
	
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
	set lbdList {7.0 5.0}
	set attList {90 150}
	for {set i 0} {$i < [llength $lbdList]} { incr i} {
		drive nvs_lambda [lindex $lbdList $i]
		drive att [lindex $attList $i]
		gumput scanSpinStateLambda: Lambda=[lindex $lbdList $i] Att=[lindex $attList $i]
		scanSpinState
	}
}

#hset /instrument/flipper/set_current 7.1
#wait 60
#hset /instrument/flipper/set_frequency 420
#wait 5
#hset /instrument/flipper/set_flip_on 0
#wait 5

#scanSpinStateLambda
scanFreqCurrentLambda

drive nvs_lambda 7.0
drive att 90
hset /instrument/flipper/set_flip_on 0
wait 60
for {set i 0} {$i < 1000} { incr i} {
	scanAnalyser
}

gumput experiment finished