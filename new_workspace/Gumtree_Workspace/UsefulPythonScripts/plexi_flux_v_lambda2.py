from time import sleep
from gumpy.commons import sics




#driveAtt(150)
sics.drive('nvs_lambda', 10)
sleep(0.1)
print 'start scanning for '
quokka.scan("time", 120)  
sleep(0.1) 
 
sics.drive('nvs_lambda', 11)
sleep(0.1)
print 'start scanning for '
quokka.scan("time", 120)  
sleep(0.1) 
 
sics.drive('nvs_lambda', 12)
sleep(0.1)
print 'start scanning for '
quokka.scan("time", 120)  
sleep(0.1) 