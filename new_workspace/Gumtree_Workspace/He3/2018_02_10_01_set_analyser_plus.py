     gumput I(MB)=1.85Amp
     he3_queue send "magnet_xyz 1.85,0,0"
     wait 5
     gumput set spin+
     he3 analyser/spin 1
     wait 5
     gumput I(MB)=3Amp
     he3_queue send "magnet_xyz 3,0,0"
     wait 5
