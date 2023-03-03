# Script control setup area
# script info
__script__.title = 'Histogram Data'
__script__.version = '1.0'

from java.io import File
from java.io import FileOutputStream
from org.apache.commons.httpclient import HttpClient
from org.apache.commons.httpclient import Credentials
from org.apache.commons.httpclient import UsernamePasswordCredentials
from org.apache.commons.httpclient.auth import AuthScope
from org.apache.commons.httpclient.methods import GetMethod

from bragg.quokka.quokka import *

PREF_NAME_FOLDER = "quokka.TOF.folder"
PREF_NAME_FILENAME = "quokka.TOF.filename"

# Initialisation
host = 'das4-quokka.nbi.ansto.gov.au'
port = 8081
user = 'Gumtree'
password = 'Gumtree'

# Use below example to create parameters.
# The type can be string, int, float, bool, file.
data_type = Par('str', 'TOTAL_HISTOGRAM_T', 
                options = ['TOTAL_HISTOGRAM_T',
                           'TOTAL_HISTOGRAM_XYT',])
data_type.title = 'Data type'
file_path = Par('file', 'C:/Temp')
file_path.dtype = 'folder'
file_path.title = 'Save folder'
filename = Par('str', 'TOF.hdf')
filename.title = 'Filename'

fd = get_pref_value(PREF_NAME_FOLDER)
if len(fd) > 0:
    file_path.value = fd
fn = get_pref_value(PREF_NAME_FILENAME)
if len(fn) > 0:
    filename.value = fn
    
# Use below example to create a button
save = Act('saveHM()', 'Save HM') 
def saveHM():
    # Create new HTTP client
    client = HttpClient()
    client.getParams().setAuthenticationPreemptive(True)
    defaultcreds = UsernamePasswordCredentials(user, password)
    client.getState().setCredentials(AuthScope.ANY, defaultcreds)
    
    # Get data across HTTP
    url = 'http://' + host + ':' + str(port) + '/admin/savedataview.egi?type=' \
        + str(data_type.value) \
        + '&data_format=NEXUSHDF5_LZW_6&data_saveopen_action=OPEN_ONLY'
    print url
    getMethod = GetMethod(url)
    getMethod.setDoAuthentication(True)
    client.executeMethod(getMethod)
    
    # Save locally
    fn = str(file_path.value) + '/' + str(filename.value)
    
    set_pref_value(PREF_NAME_FOLDER, str(file_path.value))
    set_pref_value(PREF_NAME_FILENAME, str(filename.value))
    
    fn = get_next_file(fn, 0)
    file = File(fn)
    out = FileOutputStream(file)
    out.write(getMethod.getResponseBody())
    out.close()
    print 'saved to ' + fn
    # Clean up
    getMethod.releaseConnection()


def get_next_file(inputname, idx):
    if inputname.lower().endswith('.hdf'):
        partname = inputname[:-4]
    else:
        partname = inputname
    if idx > 0:
        partname = partname + '_%03d' % (idx)
    fullname = partname + '.hdf'
    f = File(fullname)
    if f.exists():
        return get_next_file(inputname, idx + 1)
    else:
        return fullname

# Use below example to create a new Plot
# Plot4 = Plot(title = 'new plot')

# This function is called when pushing the Run button in the control UI.
def __run_script__(fns):
    # Use the provided resources, please don't remove.
    global Plot1
    global Plot2
    global Plot3
    
    saveHM()
    
    
def __dispose__():
    global Plot1
    global Plot2
    global Plot3
    Plot1.clear()
    Plot2.clear()
    Plot3.clear()
