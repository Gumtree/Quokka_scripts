drive srce 180

    set lbdList {5.0 5.76 6.0 7.0 8.0 9.0 10.0 12.0}
    set attList {150 120 120 90 60 30 0 0}
    set presetList {15000000 15600000 15000000 13800000 12000000 10200000 8400000 5400000}
    
    
    set unpolAttList {180 150 150 120 90 60 30 0}
    
    gumput Flipper on to preset values
    hset /instrument/flipper/set_flip_on 1
    wait 60
    gumput Preset Flipper current=7.1
    hset /instrument/flipper/set_current 7.1
    wait 60
    gumput Preset Flipper frequency=393
    hset /instrument/flipper/set_frequency 393
    wait 5
    gumput Flipper off
    hset /instrument/flipper/set_flip_on 0
    wait 5
    
    for {set i 0} {$i < [llength $lbdList]} { incr i} {
    	gumput Lambda=[lindex $lbdList $i] Att=[lindex $attList $i] preset=[lindex $presetList $i] 
	    
	#drive to Lambda and Att
	drive att 330
    	drive nvs_lambda [lindex $lbdList $i]
	 
	#polariser out
	gumput Unpolarised (Polariser out) 1
	drive att [lindex $unpolAttList $i]
	::optics::guide g1
	gumput Count Unpolarised 1 [lindex $presetList $i]
    	runscan dummy_motor 0 1 1 MONITOR_1 [lindex $presetList $i] datatype HISTOGRAM_XY

	#Polariser - (polariser in, flipper off)  
	gumput Polariser - (polariser in, flipper off)
	drive att 330
	::optics::guide p1
	drive att [lindex $attList $i]
	gumput Count Polariser -, Analyser + [lindex $presetList $i]
	runscan dummy_motor 0 1 1 MONITOR_1 [lindex $presetList $i] datatype HISTOGRAM_XY
       	hset /sample/isops/relay 1
    	wait 3
    	hset /sample/isops/relay 0
    	gumput Count Polariser -, Count Analyser - [lindex $presetList $i]
    	runscan dummy_motor 0 1 1 MONITOR_1 [lindex $presetList $i] datatype HISTOGRAM_XY
    	hset /sample/isops/relay 1
    	wait 3
    	hset /sample/isops/relay 0		
    	
	# configuration polariser + (polariser in, flipper on)
	gumput polariser + (polariser in, flipper on)
	hset /instrument/flipper/set_flip_on 1
	wait 60
	gumput Count Polariser +, Analyser + [lindex $presetList $i]
	runscan dummy_motor 0 1 1 MONITOR_1 [lindex $presetList $i] datatype HISTOGRAM_XY
	hset /sample/isops/relay 1
	wait 3
	hset /sample/isops/relay 0
	gumput Count Polariser +, Analyser - [lindex $presetList $i]
	runscan dummy_motor 0 1 1 MONITOR_1 [lindex $presetList $i] datatype HISTOGRAM_XY
	hset /sample/isops/relay 1
	wait 3
	hset /sample/isops/relay 0
	gumput Flipper off
	hset /instrument/flipper/set_flip_on 0
	wait 5
	
	# configuration unpol 2
	#polariser out
	gumput Unpolarised (Polariser out) 2
	drive att 330
	::optics::guide g1
	drive att [lindex $unpolAttList $i]
	gumput Count Unpolarised 2 [lindex $presetList $i]
	runscan dummy_motor 0 1 1 MONITOR_1 [lindex $presetList $i] datatype HISTOGRAM_XY
  }
    
  for {set i 0} {$i < [llength $lbdList]} { incr i} {
	  gumput Lambda=[lindex $lbdList $i] Att=[lindex $attList $i] preset=[lindex $presetList $i] 
	  
	  #drive to Lambda and Att
	  drive nvs_lambda [lindex $lbdList $i]
	  drive att [lindex $attList $i]
	  drive srce 240
	  runscan dummy_motor 0 1 1 MONITOR_1 [lindex $presetList $i] datatype HISTOGRAM_XY	  
  }
  
  
gumput experiment finished