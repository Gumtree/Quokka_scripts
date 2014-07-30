drive srce 180
drive att 330
::optics::guide p1
hset /instrument/flipper/set_flip_on 0
wait 5

    set lbdList {5.0 5.76 6.0 7.0 8.0 9.0 10.0 12.0}
    set attList {150 120 120 90 60 30 0 0}
    set presetList {3000000 3200000 5000000 2760000 2400000 2040000 1680000 1080000}
        
  for {set i 0} {$i < [llength $lbdList]} { incr i} {
	  gumput Lambda=[lindex $lbdList $i] Att=[lindex $attList $i] preset=[lindex $presetList $i] 
	  
	  #drive to Lambda and Att
	  drive nvs_lambda [lindex $lbdList $i]
	  drive att [lindex $attList $i]
	  drive srce 240
	  runscan dummy_motor 0 1 1 MONITOR_1 [lindex $presetList $i] datatype HISTOGRAM_XY	  
  }
  
  
gumput experiment finished