from java.io import File
from java.io import FileOutputStream
from org.apache.commons.httpclient import HttpClient
from org.apache.commons.httpclient import Credentials
from org.apache.commons.httpclient import UsernamePasswordCredentials
from org.apache.commons.httpclient.auth import AuthScope
from org.apache.commons.httpclient.methods import GetMethod

from bragg.quokka.quokka import *


# Initialisation
host = 'das4-quokka.nbi.ansto.gov.au'
port = 8081
type = 'TOTAL_HISTOGRAM_T'
user = 'Gumtree'
password = 'Gumtree'
#directory = 'U:/data/proposal/00100/2015/NVS_Cal_OCT2015'
#TO DO update directory
directory = r'W:\data\proposal\00105\2025\105_NVS_calibration_JK_2025_05_23'

# Fetch data from the HM server via HTTP
def saveHM(filename):
	# Create new HTTP client
	client = HttpClient()
	client.getParams().setAuthenticationPreemptive(True)
	defaultcreds = UsernamePasswordCredentials(user, password)
	client.getState().setCredentials(AuthScope.ANY, defaultcreds)
	
	# Get data across HTTP
	url = 'http://' + host + ':' + str(port) + '/admin/savedataview.egi?type=' + type + '&data_format=NEXUSHDF5_LZW_6&data_saveopen_action=OPEN_ONLY'
	print url
	getMethod = GetMethod(url)
	getMethod.setDoAuthentication(True)
	client.executeMethod(getMethod)
	
	# Save locally
	file = File(directory + '/' + filename)
	out = FileOutputStream(file)
	out.write(getMethod.getResponseBody())
	out.close()
	
	# Clean up
	getMethod.releaseConnection()

def run():
	# Assume det is at 9000 and high voltage is on
	# We collect the first set of data
	#x = 3280
	sics.clearInterrupt()
	
	RPM = 28300
	tilt = 'neg5tilt'
	att = 'att0'
	
	# To go from front to back
#	
	x = 7520
	while x <= 13520:
		sics.set('/instrument/detector/detector_y/speed', 53)
		driveDet(x)
		scan('time', 120)
		#TO DO change filename
		saveHM('TOF_NVS40_' + str(RPM) + '_' + tilt + '_ga_apx2p5_80Hz_' + att + '_' + str(x) + '.hdf')
		x = x + 1000
#	
	# To go from back to front
	
#	x = 3520
#	while x >= 520:
#		sics.set('/instrument/detector/detector_y/speed', 53)
#		driveDet(x)
#		scan('time', 180)
#		#TO DO change filename
#		saveHM('TOF_NVS40_' + str(RPM) + '_' + tilt + '_ga_apx2p5_80Hz_' + att + '_' + str(x) + '.hdf')
#		x = x - 1000
		
		
		
		
		
		
		
		