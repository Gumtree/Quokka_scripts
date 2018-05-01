drive srce 180

	#lambda {5.76 4.502 7.0}
	#attenu {270 300 240}
	set lambda 8.0
	set att 60 
	gumput Set lambda=$lambda att=$att
	drive nvs_lambda $lambda
	drive att $att
	
gumput Done