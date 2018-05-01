#drive srce 180
#initialise system with attenuated beam, beam stop in, spin flipper freq=264kHz
drive att 300
drive bsx 40
hset /instrument/flipper/set_frequency 262

proc transmissionAnalyser { } {
	set preset 180
	gumput transmissionAnalyser: Count Analyser +
	he3 analyser/spin 1
	wait 3
	runscan dummy_motor 0 1 1 time $preset datatype HISTOGRAM_XY
	gumput transmissionAnalyser: Count Analyser -
	he3 analyser/spin -1
	wait 3
	runscan dummy_motor 0 1 1 time $preset datatype HISTOGRAM_XY

}

proc scatterAnalyser { } {
	set preset 600
	gumput scatterAnalyser: Count Analyser +
	he3 analyser/spin 1
	wait 3
	runscan dummy_motor 0 1 1 time $preset datatype HISTOGRAM_XY
	gumput scatterAnalyser: Count Analyser -
	he3 analyser/spin -1
	wait 3
	runscan dummy_motor 0 1 1 time $preset datatype HISTOGRAM_XY

}

proc driveUnpolarised {} {
	gumput driveUnpolarised att 300
	drive att 300
	::optics::guide g6
}

proc transmissionUnpolarised {} {
	set preset 180
	gumput transmissionUnpolarised
	runscan dummy_motor 0 1 1 time $preset datatype HISTOGRAM_XY
				
}

proc drivePolariserIn {} {
	gumput drivePolariserIn
	drive att 300
	::optics::guide p6
}

proc transmissionSpinState { } {
	
	# configuration polariser +
	gumput transmissionSpinState: Polariser +, SF on
	hset /instrument/flipper/set_flip_on 1
	wait 60
	transmissionAnalyser
	
	# configuration polariser -
	gumput transmissionSpinState: Polariser -, SF off
	hset /instrument/flipper/set_flip_on 0
	wait 3
	transmissionAnalyser
}

proc scatteringSpinState { } {
	# configuration polariser +
	gumput scatterSpinState: Polariser + SF on
	hset /instrument/flipper/set_flip_on 1
	wait 60
	scatterAnalyser
	
	# configuration polariser -
	gumput scatterSpinState: Polariser + SF off
	hset /instrument/flipper/set_flip_on 0
	wait 3
	scatterAnalyser
}

proc scanTransmissionScatteringLambda {} {
	set lbdList {5.76 7.0 8.0}
	set attList {210 180 150}
	for {set i 0} {$i < [llength $lbdList]} { incr i} {
		gumput scanTransmissionScatteringLambda: Lambda=[lindex $lbdList $i]
		drive att 300
		drive nvs_lambda [lindex $lbdList $i]

		gumput Transmission
		gumput Drive sample out, beam stop out
		drive samz 240
		reldrive bsx 100
		gumput Unpolarised transmission att=300
		driveUnpolarised
		drive att 300
		transmissionUnpolarised
		
		gumput Polarised transmission att=[lindex $attList $i]
		drivePolariserIn
		drive att [lindex $attList $i]
		transmissionSpinState
			
		gumput Scattering
		gumput Drive sample in, beam stop in, att=0
		drive samz 287.5
		reldrive bsx -100
		drive att 0
		scatteringSpinState
	}
}

gumput drive sample in
drive samx -10.5
drive samz 287.5

scanTransmissionScatteringLambda
scanTransmissionScatteringLambda

gumput experiment finished