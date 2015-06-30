
proc scanPolariser { } {
	set preset 3000000
	gumput scanFreq: Flipper on, measure
	hset /instrument/flipper/set_flip_on 1
	wait 60
	runscan dummy_motor 0 1 1 MONITOR_1 $preset datatype HISTOGRAM_XY

	gumput scanFreq: Flipper off, measure
	hset /instrument/flipper/set_flip_on 0
	wait 60
	runscan dummy_motor 0 1 1 MONITOR_1 $preset datatype HISTOGRAM_XY
}

#set lambda 7.0
#set att 90
#gumput lambda=$lambda, att=$att
#drive nvs_lambda $lambda
#drive att $att
#wait 60

#set current 7.1
#set frequency 385
#gumput scanCurrent: Flipper Current = $current
#hset /instrument/flipper/set_current $current
#wait 60
#gumput Flipper Freq = $frequency
#hset /instrument/flipper/set_frequency $frequency
#wait 3
#for {set i 0} {$i < 1000} { incr i} {
#	scanPolariser
#}
scanPolariser

gumput experiment finished