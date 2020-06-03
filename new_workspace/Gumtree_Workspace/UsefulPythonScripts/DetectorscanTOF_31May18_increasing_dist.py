from java.io import File
from java.io import FileOutputStream
from org.apache.commons.httpclient import HttpClient
from org.apache.commons.httpclient import Credentials
from org.apache.commons.httpclient import UsernamePasswordCredentials
from org.apache.commons.httpclient.auth import AuthScope
from org.apache.commons.httpclient.methods import GetMethod

from bragg.quokka.quokka import *


# Initialisation
host = 'das1-quokka.nbi.ansto.gov.au'
port = 8081
type = 'TOTAL_HISTOGRAM_T'
user = 'Gumtree'
password = 'Gumtree'
#directory = 'U:/data/proposal/00100/2015/NVS_Cal_OCT2015'
directory = r'U:\data\proposal\00100\2018\AgBe and NVS 43 calibration 31 May 2018'

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
	x = 1200
	while x <= 7200:
		sics.set('/instrument/detector/detector_y/speed', 53)
		driveDet(x)
		scan('time', 600)
		saveHM('TOF_0R_12242_NVS43_ga_apx2p5_off_80Hz_180531' + str(x) + '.hdf')
		x = x + 1500
		
		
		
		
		
		
		
		