
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
     wait 5
     gumput set spin+
     he3 analyser/spin 1
     wait 5
     gumput I(MB)=3Amp
     he3_queue send "magnet_xyz 3,0,0"
     wait 5
} 

proc set_spin_minus { } {
     gumput I(MB)=1.85Amp
     he3_queue send "magnet_xyz 1.85,0,0"
     wait 5
     gumput set spin-
     he3 analyser/spin -1
     wait 5
     gumput I(MB)=3Amp
     he3_queue send "magnet_xyz 3,0,0"
     wait 5
} 

gumput 
doCount120
gumput set spin minus
set_spin_minus
doCount120
gumput set spin plus
set_spin_plus



