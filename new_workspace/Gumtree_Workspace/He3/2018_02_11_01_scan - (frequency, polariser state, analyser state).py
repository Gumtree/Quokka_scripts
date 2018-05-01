
proc doCount120 { } {
     newfile HISTOGRAM_XY
     histmem mode time
     histmem preset 120 
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
     doCount120
     gumput set spin minus
     set_spin_minus
     doCount120
     gumput set spin plus
     set_spin_plus
}

proc scanFreq { } {
    set freqList {250 245 240 235 230 225 220 215 210}
    for {set j 0} {$j < [llength $freqList]} { incr j} {
        gumput scanFreq: Flipper Freq = [lindex $freqList $j]
        hset /instrument/flipper/set_frequency [lindex $freqList $j]
        wait 5
        gumput scanFreq: (off) measure, on, measure, off
        measure_flipping_ratio
        hset /instrument/flipper/set_flip_on 1
        wait 60
        measure_flipping_ratio
        hset /instrument/flipper/set_flip_on 0
        wait 60        
    }

}

scanFreq


