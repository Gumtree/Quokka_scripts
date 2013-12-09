from gumpy.commons import sics
from gumpy.commons import logger
from bragg.quokka import workflow
from bragg.quokka.quokka import *
from time import sleep
import logging, sys, traceback
log = logger.log

###############################################################################
#
# House keeping routines
#
###############################################################################

# Setup experiment
def setup():
    # User details
    print
    log('Setting user details')
    sics.set('user', 'EPG and Marta')
    sics.set('email', 'null')
    sics.set('phone', 'null')
    # Experiment details
    print
    log('Setting experiment details')
    sics.set('title', 'Food Science Programme PP1480')

# Clean up
def cleanUp():
    print
    log('Clean up')
    try:
        sleep(1)
        driveAtt(330)
        if workflow.isDriveSampleStage():
            driveToLoadPosition()
    except SicsExecutionException :
        traceback.print_exc(file=__context__.errorWriter)
        logger.__global_writer__ = None
        raise SicsExecutionException, 'SICS Interrupted'
    except:
        traceback.print_exc(file=__context__.errorWriter)
        logger.__global_writer__ = None
    print
    log('Experiment has been completed')

###############################################################################
#
# L1=L2=20m_central_flux_apx10 config routines
#
###############################################################################

# Initial rountine for L1=L2=20m_central_flux_apx10 config
def driveToConfig0():
    # Drive attenuator to safe value
    driveAtt(330)
    sics.drive('nvs_lambda', 5.0)
    # Drive detector to short position
    sics.set('/instrument/detector/detector_y/speed', 53)
    driveDet(19250,0)
    # Drive guide to ga config
    driveGuide(guideConfig.ga)
    # Drive entrance aperture to 150 (for ga)
    driveEntRotAp(150)
    #set sample ap to 10 mm
    sics.drive('apx', -72)
    # Drive beamstops up
    selBs(1)
    sics.set('beamcenterx', 97.3555)
    sics.set('beamcenterz', 94.9263)
    pass

# Pre-transmission rountine for L1=L2=20m_central_flux_apx10 config
def driveToConfig0Transmission():
    # Move the beamstop out
    driveBsx(32, 100)
    # Drive attenuator to 240
    driveAtt(240)
    pass

# Pre-scattering rountine for L1=L2=20m_central_flux_apx10 config
def driveToConfig0Scattering():
    # Drive attenuator to safe value
    driveAtt(330)
    # Move the beamstop in
    driveBsx(32, 0)
    driveBsz(252.0)
    pass

###############################################################################
#
# Settings
#
###############################################################################

# Instrument configuration dictionary
configs = {
    '0-L1=L2=20m_central_flux_apx10':{
        'name':'L1=L2=20m_central_flux_apx10',
        'mainRoutine':driveToConfig0,
        'manualAttenuationAlgorithm':False,
        'startingAttenuation':60,
        'transmissionRoutine':driveToConfig0Transmission,
        'transmissionMode':scanMode.time,
        'transmissionPreset':30,
        'scatteringRoutine':driveToConfig0Scattering,
        'scatteringMode':scanMode.time,
    },
}

# Sample dictionary
samples = {
    1:{'position':1, 'name':'Cellulose in H2O', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    2:{'position':2, 'name':'Cellulose in D2O', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    3:{'position':3, 'name':'Cellulose xyloglucans in H2O', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    4:{'position':4, 'name':'Cellulose xyloglucans in D2O', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    5:{'position':5, 'name':'Cellulose arabinoxylans in H2O', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    6:{'position':6, 'name':'Cellulose arabinoxylans in D2O', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    7:{'position':7, 'name':'H2O', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    8:{'position':8, 'name':'D2O', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    9:{'position':9, 'name':'MT demountable', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    10:{'position':10, 'name':'Blocked beam for Hellma', 'type':'sample', 'description':'UNKNOWN', 'thickness':'0.0'},
    20:{'position':20, 'name':'MT beam', 'type':'empty_beam', 'description':'UNKNOWN', 'thickness':'0.0'},
}

# Acquisition dictionary
acqusitionEntries = (
    {
        'type':'config', 'target':'0-L1=L2=20m_central_flux_apx10', 'contents':(
            {'seq':0, 'sample':1, 'runId':0, 'preset':5400},
            {'seq':1, 'sample':2, 'runId':1, 'preset':2700},
            {'seq':2, 'sample':3, 'runId':2, 'preset':5400},
            {'seq':3, 'sample':4, 'runId':3, 'preset':2700},
            {'seq':4, 'sample':5, 'runId':4, 'preset':5400},
            {'seq':5, 'sample':6, 'runId':5, 'preset':2700},
            {'seq':6, 'sample':7, 'runId':6, 'preset':3600},
            {'seq':7, 'sample':8, 'runId':7, 'preset':2400},
            {'seq':8, 'sample':9, 'runId':8, 'preset':1800},
            {'seq':9, 'sample':10, 'runId':9, 'preset':1800},
            {'seq':10, 'sample':20, 'runId':10, 'preset':60},
        )
    },
)

###############################################################################
#
# Experiment logic
#
###############################################################################

if __name__ == '__main__':
    
    logger.__global_writer__ = __context__.writer
    # Set up
    setup()
    
    # Set global settings
    workflow.configs = configs
    workflow.samples = samples
    workflow.engineContext = __context__
    
    # Start looping through configurations
    try:
        workflow.runQuokkaScan(acqusitionEntries)
    except:
        logging.error('Exception occured. It will now go to clean up mode.')
        log('Exception occured. It will now go to clean up mode.')
        # Save result
        log('Saving intermediate result')
        sics.execute('newfile HISTOGRAM_XY')
        sics.execute('save')
        traceback.print_exc(file=__context__.errorWriter)
        log(str(sys.exc_info()))
    
    # Clean up
    cleanUp()
    logger.__global_writer__ = None

