#drive srce 180
#initialise system with attenuated beam, beam stop out, spin flipper freq=264kHz
drive att 300
drive bsx 140
hset /instrument/flipper/set_frequency 264

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
	
	# configuration polariser -
	gumput transmissionSpinState: Polariser -, SF off
	hset /instrument/flipper/set_flip_on 0
	wait 3
	transmissionAnalyser
}


proc scanTransmissionLambda {} {
	gumput Transmission
	gumput Drive sample out
	drive samz 240

	gumput scanTransmissionScatteringLambda: Lambda=5.76
	drive att 300
	drive nvs_lambda 5.76

	gumput Polarised transmission att=210
	drivePolariserIn
	drive att 210
	transmissionSpinState
			
	gumput Unpolarised transmission att=300
	driveUnpolarised
	drive att 300
	transmissionUnpolarised
		
        gumput scanTransmissionScatteringLambda: Lambda=7
        drive att 300
        drive nvs_lambda 7.0
        
        gumput Unpolarised transmission att=300
        driveUnpolarised
        drive att 300
        	
        transmissionUnpolarised
        gumput scanTransmissionScatteringLambda: Lambda=8
        drive att 300
        drive nvs_lambda 8.0
        
        gumput Unpolarised transmission att=300
        driveUnpolarised
        drive att 300
        transmissionUnpolarised
}

scanTransmissionLambda

gumput drive Magic Box out
drive samz 6
drive samx 460

gumput experiment finished