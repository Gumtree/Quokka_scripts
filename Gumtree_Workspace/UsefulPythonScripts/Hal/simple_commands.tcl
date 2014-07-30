drive srce 180

	#polariser in
	gumput Polariser in
	::optics::guide p1

	#polariser out
	gumput Polariser out
	::optics::guide g1

	#Flipper off
	gumput Flipper on
	hset /instrument/flipper/set_flip_on 0
	wait 60

	#Flipper on, set current & frequency
	gumput Flipper on
	hset /instrument/flipper/set_flip_on 1
	wait 60

	set freq 407
	gumput Set Flipper Frequency = $freq
	hset /instrument/flipper/set_frequency $freq
	wait 5
	
	set current 7.1
	gumput Set Flipper Current = $current
	hset /instrument/flipper/set_frequency $current
	wait 60
	
	#lambda {5.76 4.502 7.0}
	#attenu {270 300 240}
	set lambda 5.76
	set att 270 
	gumput Set lambda=$lambda att=$att
	drive nvs_lambda $lambda
	drive att $att
	
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