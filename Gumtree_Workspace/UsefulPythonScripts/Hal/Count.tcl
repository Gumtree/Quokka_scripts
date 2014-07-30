drive srce 180

	#count analyser
	set preset 7500000
	gumput Count $preset
	runscan dummy_motor 0 1 1 MONITOR_1 $preset datatype HISTOGRAM_XY
gumput Done