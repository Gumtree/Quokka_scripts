from java.io import File
from java.io import FileOutputStream
from org.apache.commons.httpclient import HttpClient
from org.apache.commons.httpclient import Credentials
from org.apache.commons.httpclient import UsernamePasswordCredentials
from org.apache.commons.httpclient.auth import AuthScope
from org.apache.commons.httpclient.methods import GetMethod
import time
from Internal import sicsext
import random

# Initialisation
host = 'das4-quokka.nbi.ansto.gov.au'
port = 8081
type = 'TOTAL_HISTOGRAM_T'
user = 'Gumtree'
password = 'Gumtree'
#directory = 'U:/data/proposal/00100/2015/NVS_Cal_OCT2015'
directory = r'U:/data/proposal/07609'
HMM_FILENAME = 'lambda_scan_'

#Loop_start = 5
#Loop_stop = 50
#Loop_step_size = 10

Collection_preset = 240
#TIME_WAIT_SPEED_CHANGE = 120

LOOP_VALUES = [4.75, 5, 6, 7, 8, 9]

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
	
#	x = Loop_start
#	while x <= Loop_stop:
	for val in LOOP_VALUES:
#		sics.set('/instrument/detector/detector_y/speed', val)
#		time.sleep(TIME_WAIT_SPEED_CHANGE)
		sics.drive('nvs_lambda', val)
		time.sleep(1)
#		driveDet(x, getDetOffsetValue())
#		quokka.scan(scanMode.time, dataType.HISTOGRAM_XYT, 600, 'true', saveType.nosave)
		sicsext.runscan('dummy_motor', 0, 0, 1, 'time', Collection_preset, datatype = 'HISTOGRAM_XYT')
		saveHM(HMM_FILENAME + str(val) + '_' +  str(random.randint(0, 1000000)) + '.hdf')
		time.sleep(3)
#		x = x + Loop_step_size