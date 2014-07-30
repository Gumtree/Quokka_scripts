drive srce 180

	#count analyser
	set preset 7500000
	gumput Analyser +, Count $preset
	runscan dummy_motor 0 1 1 MONITOR_1 $preset datatype HISTOGRAM_XY
	hset /sample/isops/relay 1
	wait 3
	hset /sample/isops/relay 0
	gumput Analyser -, Count $preset
	runscan dummy_motor 0 1 1 MONITOR_1 $preset datatype HISTOGRAM_XY
	hset /sample/isops/relay 1
	wait 3
	hset /sample/isops/relay 0

gumput Done