
proc doCount300 { } {
     newfile HISTOGRAM_XY
     histmem mode time
     histmem preset 300 
     histmem start block
     save
}

proc set_spin_plus { } {
     gumput I(MB)=1.85Amp
     he3_queue send "magnet_xyz 1.85,0,0"
     wait 60
     gumput set spin+
     he3 analyser/spin 1
     wait 2
     gumput I(MB)=3Amp
     he3_queue send "magnet_xyz 3,0,0"
     wait 60
} 

proc set_spin_minus { } {
     gumput I(MB)=1.85Amp
     he3_queue send "magnet_xyz 1.85,0,0"
     wait 60
     gumput set spin-
     he3 analyser/spin -1
     wait 2
     gumput I(MB)=3Amp
     he3_queue send "magnet_xyz 3,0,0"
     wait 60
} 

proc measure_flipping_ratio { } {
     doCount300
     gumput set spin minus
     set_spin_minus
     doCount300
     gumput set spin plus
     set_spin_plus
}

proc measure_analyser_transmission { } {
     drive att 300
     drive srce 30
     drive att 150
     ::optics::guide g1
     doCount300
     ::optics::guide p1
     drive att 60
}

proc scanSRCE { } {
    set srceList {150 120 90 60 30 0}
    for {set i 0} {$i < [llength $srceList]} { incr i} {
        gumput scanSRCE: srce=[lindex $srceList $i]
        drive att 300
        drive srce [lindex $srceList $i]
        drive att 60
        measure_flipping_ratio
        measure_analyser_transmission
    }
}

proc doCount600 { } {
     newfile HISTOGRAM_XY
     histmem mode time
     histmem preset 600 
     histmem start block
     save
}

proc measureT1{ } {
    drive att 300
    drive srce 30
    drive att 150
    ::optics::guide g1
    for {set i 0} {$i < 1000} { incr i} {
       doCount600
    }
} 
#set_spin_plus
measure_analyser_transmission
scanSRCE
measureT1

