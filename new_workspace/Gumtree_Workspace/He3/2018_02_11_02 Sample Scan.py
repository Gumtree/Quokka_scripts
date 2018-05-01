
proc doCount { t } {
     gumput count $t
     newfile HISTOGRAM_XY
     histmem mode time
     histmem preset $t 
     histmem start block
     save
}

proc setSpin { device spin } {
     if {$device eq "polariser" && $spin eq "+"} {
         gumput set polariser +
         hset /instrument/flipper/set_flip_on 1
         wait 60
     } elseif {$device eq "polariser" && $spin eq "-"} {
         gumput set polariser -
         hset /instrument/flipper/set_flip_on 0
         wait 10
     } elseif {$device eq "analyser" && $spin eq "+"} {
         gumput set analyser +
         gumput I(MB)=1.85Amp
         he3_queue send "magnet_xyz 1.85,0,0"
         wait 5
         he3 analyser/spin 1
         wait 5
         gumput I(MB)=3Amp
         he3_queue send "magnet_xyz 3,0,0"
         wait 5
     } elseif {$device eq "analyser" && $spin eq "-"} {
         gumput set analyser -
         gumput I(MB)=1.85Amp
         he3_queue send "magnet_xyz 1.85,0,0"
         wait 5
         he3 analyser/spin -1
         wait 5
         gumput I(MB)=3Amp
         he3_queue send "magnet_xyz 3,0,0"
         wait 5
     } else {
         gumput wrong polariser command
         wait 1
     }
} 

proc doCalibrationScan { t1 t2 } {
# measure direct beam flipping ratio
#start with +- state, end with ++ state
     drive att 300
     drive samz 50
     reldrive bsx 100
     drive att 150
     
     gumput calibrate +-
     doCount $t2
     gumput calibrate ++
     setSpin analyser +
     doCount $t2
     gumput calibrate -+
     setSpin polariser -
     doCount $t2
     gumput calibrate --
     setSpin analyser -
     doCount $t2

#measure analyser transmission
     gumput calibrate analyser transmission
     drive att 300
     ::optics::guide g1
     drive att 180
     doCount $t1

     drive att 300
     reldrive bsx -100
     ::optics::guide p1
     drive samz 128
     drive att 0
}

proc doScan { t1 t2 } {
    gumput sample ++
    doCount $t1
    
    gumput sample -+
    setSpin polariser -
    doCount $t1
    
    gumput sample --
    setSpin analyser -
    doCount $t1
    
    gumput sample +-
    setSpin polariser +
    doCount $t1
    
    gumput calibration scan
    doCalibrationScan $t1 $t2
    
    gumput sample +-
    setSpin polariser +
    doCount $t1
    
    gumput sample --
    setSpin polariser -
    doCount $t1
    
    gumput sample -+
    setSpin analyser +
    doCount $t1
    
    gumput sample ++
    setSpin polariser +
    doCount $t1
}

#sample scan starts with beam stop in, guide=p5, samz=128, att=300
set t1 300
set t2 120

setSpin polariser +
setSpin analyser -
doCalibrationScan $t1 $t2
setSpin polariser +
setSpin analyser +

for {set i 0} {$i < 1000} { incr i} {
    doScan $t1 $t2
} 

