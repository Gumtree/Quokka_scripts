#assuming two sample positions
#samx = 40 is Ag behenate
#samx = 5 is paraffin
#current config is p5 (polarised)
#lambda = 8 A
#resolution = 10%
#collect scattering data on AgBe

    set preset 3000000
    gumput scanAnalyser: Count Analyser +
    he3 analyser/spin 1
    wait 2
    he3 analyser/spin 0
    wait 2
    runscan dummy_motor 0 1 1 MONITOR_1 $preset datatype HISTOGRAM_XY
    gumput scanAnalyser: Count Analyser -
    he3 analyser/spin -1
    wait 2
    he3 analyser/spin 0
    wait 2
    runscan dummy_motor 0 1 1 MONITOR_1 $preset datatype HISTOGRAM_XY


#silver ????? 
#check spin status
