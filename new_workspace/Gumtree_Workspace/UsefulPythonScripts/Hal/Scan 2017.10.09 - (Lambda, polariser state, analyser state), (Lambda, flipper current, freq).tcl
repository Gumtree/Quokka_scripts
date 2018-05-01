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
	
	# configuration polariser +
	gumput scanSpinState: Polariser + SF on
	hset /instrument/flipper/set_flip_on 1
	wait 60
	scanAnalyser
	
	# configuration polariser -
	# Drive flipper
	gumput scanSpinState: Polariser + SF off
	hset /instrument/flipper/set_flip_on 0
	wait 3
	scanAnalyser
}

proc scanSpinStateFreq { } {
	set freqList {253 255}
	
	#polariser in
	gumput drive polariser in - p1
	::optics::guide p1	
	run att 270
	
	for {set j 0} {$j < [llength $freqList]} { incr j} {
		gumput scanSpinStateFreq: Flipper Freq = [lindex $freqList $j]
		hset /instrument/flipper/set_frequency [lindex $freqList $j]
		wait 3
		scanSpinState	
	}
}

proc scanUnpolaised {} {
	set preset 180
	run att 300
	# configuration unpol 1
	gumput drive polariser out - g1
	::optics::guide g1
	#don't change below scan command
	gumput scanUnpolaised: Count
	runscan dummy_motor 0 1 1 time $preset datatype HISTOGRAM_XY

}


#hset /instrument/flipper/set_current 7.1
#wait 60
#hset /instrument/flipper/set_frequency 385
#wait 5
#hset /instrument/flipper/set_flip_on 0
#wait 5

gumput wavelength=5.76A
gumput drive MB in
#drive samx -10.5
#drive samz 287.5

scanSpinStateFreq
scanUnpolaised

drive samz 287.5
drive samx -10.5

gumput experiment finished