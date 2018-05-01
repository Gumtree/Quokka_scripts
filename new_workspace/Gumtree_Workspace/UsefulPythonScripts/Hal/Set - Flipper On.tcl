	#Flipper on, set current & frequency
	gumput Flipper on
	hset /instrument/flipper/set_flip_on 1
	wait 60

	set freq 397
	gumput Set Flipper Frequency = $freq
	hset /instrument/flipper/set_frequency $freq
	wait 5
	
	set current 7.1
	gumput Set Flipper Current = $current
	hset /instrument/flipper/set_current $current
	wait 60

gumput Done