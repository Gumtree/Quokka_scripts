drive srce 180
hset /instrument/flipper/set_flip_on 0
::optics::guide p1


    set lbdList {5.0 5.76 6.0 7.0 8.0 9.0 10.0 12.0}
    set attList {150 120 120 90 60 30 0 0}
    set presetList {4500000 4680000 4500000 4140000 3600000 3060000 2520000 1620000}
    set unpolAttList {180 150 150 120 90 60 30 0}

    gumput Test depolarisation (Lambda=8.0 Att=60 preset=3600000)
    gumput The next 2 should gives similar counts
    drive att 330
    drive nvs_lambda 8.0
    ::optics::guide p1
    drive att 60
    gumput Count Polariser -, Count Analyser + 3600000
    runscan dummy_motor 0 1 1 MONITOR_1 3600000 datatype HISTOGRAM_XY
    hset /sample/isops/relay 1
    wait 3
    hset /sample/isops/relay 0
    gumput Count Polariser -, Count Analyser - 3600000
    runscan dummy_motor 0 1 1 MONITOR_1 3600000 datatype HISTOGRAM_XY
    hset /sample/isops/relay 1
    wait 3
    hset /sample/isops/relay 0		
    gumput test done. If the counts differ too much, cell needs depolarising again.
    
    
    for {set i 0} {$i < [llength $lbdList]} { incr i} {
    	gumput Lambda=[lindex $lbdList $i] Att=[lindex $attList $i] preset=[lindex $presetList $i] 
	    
	#drive to Lambda and Att
	drive att 330
    	drive nvs_lambda [lindex $lbdList $i]
	 
	#polariser out
	gumput Unpolarised (Polariser out) 1
	::optics::guide g1
	drive att [lindex $unpolAttList $i]
	gumput Count Unpolarised 1 [lindex $presetList $i]
    	runscan dummy_motor 0 1 1 MONITOR_1 [lindex $presetList $i] datatype HISTOGRAM_XY

	#Polariser - (polariser in, flipper off)  
	gumput Polariser - (polariser in, flipper off)
	drive att 330
	::optics::guide p1
	drive att [lindex $attList $i]
	gumput Count Polariser -, Analyser + [lindex $presetList $i]
	runscan dummy_motor 0 1 1 MONITOR_1 [lindex $presetList $i] datatype HISTOGRAM_XY

}
  
gumput experiment finished