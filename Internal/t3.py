from gumpy.commons import sics
from bragg.quokka import workflow
from bragg.quokka.quokka import *
from time import sleep
import logging, sys, traceback

###############################################################################
#
# House keeping routines
#
###############################################################################

# Setup experiment
def setup():
    # User details
    print
    print 'Setting user details'
    sics.set('user', 'null')
    sics.set('email', 'null')
    sics.set('phone', 'null')
    # Experiment details
    print
    print 'Setting experiment details'
    sics.set('title', 'null')

# Clean up
def cleanUp():
    print
    print 'Clean up'
    sleep(1)
    driveAtt(330)
    if workflow.isDriveSampleStage():
        driveToLoadPosition()
    print
    print 'Experiment has been completed'

###############################################################################
#
# L1=L2=8m_offset_apx12.5_Aug2013 config routines
#
###############################################################################

# Initial rountine for L1=L2=8m_offset_apx12.5_Aug2013 config
def driveToConfig0():
    # Drive attenuator to safe value
    driveAtt(330)
    #sics.drive('nvs_lambda', 5.0)
    # Drive detector to short position
    #sics.set('/instrument/detector/detector_y/speed', 53)
    driveDet(7200,300)
    # Drive guide to g5 config
    driveGuide(guideConfig.g5)
    # Drive entrance aperture to 180 (for g5)
    driveEntRotAp(180)
    #set sample ap to 12.5 mm
    sics.drive('apx', -98)
    # Drive beamstops up
    selBs(1)
    sics.set('beamcenterx',38.53)
    sics.set('beamcenterz', 95.98)
    pass

# Pre-transmission rountine for L1=L2=8m_offset_apx12.5_Aug2013 config
def driveToConfig0Transmission():
    # Move the beamstop out
    driveBsx(32.5, 100)
    # Drive attenuator to 300
    driveAtt(300)
    pass

# Pre-scattering rountine for L1=L2=8m_offset_apx12.5_Aug2013 config
def driveToConfig0Scattering():
    # Drive attenuator to safe value
    driveAtt(330)
    # Move the beamstop in
    driveBsx(32.5,0)
    driveBsz(258.0)
    pass

###############################################################################
#
# L1=L2=8m_offset_apx12.5_Aug2013 config routines
#
###############################################################################

# Initial rountine for L1=L2=8m_offset_apx12.5_Aug2013 config
def driveToConfig1():
    # Drive attenuator to safe value
    driveAtt(330)
    #sics.drive('nvs_lambda', 5.0)
    # Drive detector to short position
    #sics.set('/instrument/detector/detector_y/speed', 53)
    driveDet(7200,300)
    # Drive guide to g5 config
    driveGuide(guideConfig.g5)
    # Drive entrance aperture to 180 (for g5)
    driveEntRotAp(180)
    #set sample ap to 12.5 mm
    sics.drive('apx', -98)
    # Drive beamstops up
    selBs(1)
    sics.set('beamcenterx',38.53)
    sics.set('beamcenterz', 95.98)
    pass

# Pre-transmission rountine for L1=L2=8m_offset_apx12.5_Aug2013 config
def driveToConfig1Transmission():
    # Move the beamstop out
    driveBsx(32.5, 100)
    # Drive attenuator to 300
    driveAtt(300)
    pass

# Pre-scattering rountine for L1=L2=8m_offset_apx12.5_Aug2013 config
def driveToConfig1Scattering():
    # Drive attenuator to safe value
    driveAtt(330)
    # Move the beamstop in
    driveBsx(32.5,0)
    driveBsz(258.0)
    pass

###############################################################################
#
# L1=L2=8m_offset_apx12.5_Aug2013 config routines
#
###############################################################################

# Initial rountine for L1=L2=8m_offset_apx12.5_Aug2013 config
def driveToConfig2():
    # Drive attenuator to safe value
    driveAtt(330)
    #sics.drive('nvs_lambda', 5.0)
    # Drive detector to short position
    #sics.set('/instrument/detector/detector_y/speed', 53)
    driveDet(7200,300)
    # Drive guide to g5 config
    driveGuide(guideConfig.g5)
    # Drive entrance aperture to 180 (for g5)
    driveEntRotAp(180)
    #set sample ap to 12.5 mm
    sics.drive('apx', -98)
    # Drive beamstops up
    selBs(1)
    sics.set('beamcenterx',38.53)
    sics.set('beamcenterz', 95.98)
    pass

# Pre-transmission rountine for L1=L2=8m_offset_apx12.5_Aug2013 config
def driveToConfig2Transmission():
    # Move the beamstop out
    driveBsx(32.5, 100)
    # Drive attenuator to 300
    driveAtt(300)
    pass

# Pre-scattering rountine for L1=L2=8m_offset_apx12.5_Aug2013 config
def driveToConfig2Scattering():
    # Drive attenuator to safe value
    driveAtt(330)
    # Move the beamstop in
    driveBsx(32.5,0)
    driveBsz(258.0)
    pass

###############################################################################
#
# Settings
#
###############################################################################

# Instrument configuration dictionary
configs = {
    '0-L1=L2=8m_offset_apx12.5_Aug2013':{
        'name':'L1=L2=8m_offset_apx12.5_Aug2013',
        'mainRoutine':driveToConfig0,
        'manualAttenuationAlgorithm':True,
        'startingAttenuation':180,
        'transmissionRoutine':driveToConfig0Transmission,
        'transmissionMode':scanMode.time,
        'transmissionPreset':30,
        'scatteringRoutine':driveToConfig0Scattering,
        'scatteringMode':scanMode.time,
    },
    '1-L1=L2=8m_offset_apx12.5_Aug2013':{
        'name':'L1=L2=8m_offset_apx12.5_Aug2013',
        'mainRoutine':driveToConfig1,
        'manualAttenuationAlgorithm':True,
        'startingAttenuation':180,
        'transmissionRoutine':driveToConfig1Transmission,
        'transmissionMode':scanMode.time,
        'transmissionPreset':30,
        'scatteringRoutine':driveToConfig1Scattering,
        'scatteringMode':scanMode.time,
    },
    '2-L1=L2=8m_offset_apx12.5_Aug2013':{
        'name':'L1=L2=8m_offset_apx12.5_Aug2013',
        'mainRoutine':driveToConfig2,
        'manualAttenuationAlgorithm':True,
        'startingAttenuation':180,
        'transmissionRoutine':driveToConfig2Transmission,
        'transmissionMode':scanMode.time,
        'transmissionPreset':30,
        'scatteringRoutine':driveToConfig2Scattering,
        'scatteringMode':scanMode.time,
    },
}

# Sample dictionary
samples = {
    1:{'position':1, 'name':'1', 'type':'sample', 'description':'1', 'thickness':'1.0'},
    2:{'position':2, 'name':'2', 'type':'sample', 'description':'2', 'thickness':'1.0'},
    3:{'position':3, 'name':'3', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    4:{'position':4, 'name':'4', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    5:{'position':5, 'name':'5', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    6:{'position':6, 'name':'6', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    7:{'position':7, 'name':'UNKNOWN', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    8:{'position':8, 'name':'UNKNOWN', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    9:{'position':9, 'name':'UNKNOWN', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    10:{'position':10, 'name':'UNKNOWN', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    11:{'position':11, 'name':'UNKNOWN', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    12:{'position':12, 'name':'UNKNOWN', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    13:{'position':13, 'name':'UNKNOWN', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    14:{'position':14, 'name':'UNKNOWN', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    15:{'position':15, 'name':'UNKNOWN', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    16:{'position':16, 'name':'UNKNOWN', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    17:{'position':17, 'name':'UNKNOWN', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    18:{'position':18, 'name':'UNKNOWN', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    19:{'position':19, 'name':'UNKNOWN', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    20:{'position':20, 'name':'UNKNOWN', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
}

# Sample environment dictionary
sampleEnvironments = {
    # Sample environment dummy_motor
    '0-dummy_motor':{
        'controller':'dummy_motor',
        0:{'preset':1.0, 'wait':1},
        1:{'preset':2.0, 'wait':1},
        2:{'preset':3.0, 'wait':1},
        3:{'preset':4.0, 'wait':1},
        4:{'preset':5.0, 'wait':1},
    },
}

# Acquisition dictionary
acqusitionEntries = (
    {
        'type':'sampleEnv', 'target':'0-dummy_motor', 'setting':0, 'contents':(
            {
                'type':'config', 'target':'0-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':1, 'runId':0, 'preset':60},
                    {'seq':1, 'sample':2, 'runId':1, 'preset':60},
                    {'seq':2, 'sample':3, 'runId':2, 'preset':60},
                    {'seq':3, 'sample':4, 'runId':3, 'preset':60},
                    {'seq':4, 'sample':5, 'runId':4, 'preset':60},
                    {'seq':5, 'sample':6, 'runId':5, 'preset':60},
                    {'seq':6, 'sample':7, 'runId':6, 'preset':60},
                    {'seq':7, 'sample':8, 'runId':7, 'preset':60},
                    {'seq':8, 'sample':9, 'runId':8, 'preset':60},
                    {'seq':9, 'sample':10, 'runId':9, 'preset':60},
                    {'seq':10, 'sample':11, 'runId':10, 'preset':60},
                    {'seq':11, 'sample':12, 'runId':11, 'preset':60},
                    {'seq':12, 'sample':13, 'runId':12, 'preset':60},
                    {'seq':13, 'sample':14, 'runId':13, 'preset':60},
                    {'seq':14, 'sample':15, 'runId':14, 'preset':60},
                    {'seq':15, 'sample':16, 'runId':15, 'preset':60},
                    {'seq':16, 'sample':17, 'runId':16, 'preset':60},
                    {'seq':17, 'sample':18, 'runId':17, 'preset':60},
                    {'seq':18, 'sample':19, 'runId':18, 'preset':60},
                    {'seq':19, 'sample':20, 'runId':19, 'preset':60},
                )
            },
            {
                'type':'config', 'target':'1-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':1, 'runId':20, 'preset':60},
                    {'seq':1, 'sample':2, 'runId':21, 'preset':60},
                    {'seq':2, 'sample':3, 'runId':22, 'preset':60},
                    {'seq':3, 'sample':4, 'runId':23, 'preset':60},
                    {'seq':4, 'sample':5, 'runId':24, 'preset':60},
                    {'seq':5, 'sample':6, 'runId':25, 'preset':60},
                    {'seq':6, 'sample':7, 'runId':26, 'preset':60},
                    {'seq':7, 'sample':8, 'runId':27, 'preset':60},
                    {'seq':8, 'sample':9, 'runId':28, 'preset':60},
                    {'seq':9, 'sample':10, 'runId':29, 'preset':60},
                    {'seq':10, 'sample':11, 'runId':30, 'preset':60},
                    {'seq':11, 'sample':12, 'runId':31, 'preset':60},
                    {'seq':12, 'sample':13, 'runId':32, 'preset':60},
                    {'seq':13, 'sample':14, 'runId':33, 'preset':60},
                    {'seq':14, 'sample':15, 'runId':34, 'preset':60},
                    {'seq':15, 'sample':16, 'runId':35, 'preset':60},
                    {'seq':16, 'sample':17, 'runId':36, 'preset':60},
                    {'seq':17, 'sample':18, 'runId':37, 'preset':60},
                    {'seq':18, 'sample':19, 'runId':38, 'preset':60},
                    {'seq':19, 'sample':20, 'runId':39, 'preset':60},
                )
            },
            {
                'type':'config', 'target':'2-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':1, 'runId':40, 'preset':60},
                    {'seq':1, 'sample':2, 'runId':41, 'preset':60},
                    {'seq':2, 'sample':3, 'runId':42, 'preset':60},
                    {'seq':3, 'sample':4, 'runId':43, 'preset':60},
                    {'seq':4, 'sample':5, 'runId':44, 'preset':60},
                    {'seq':5, 'sample':6, 'runId':45, 'preset':60},
                    {'seq':6, 'sample':7, 'runId':46, 'preset':60},
                    {'seq':7, 'sample':8, 'runId':47, 'preset':60},
                    {'seq':8, 'sample':9, 'runId':48, 'preset':60},
                    {'seq':9, 'sample':10, 'runId':49, 'preset':60},
                    {'seq':10, 'sample':11, 'runId':50, 'preset':60},
                    {'seq':11, 'sample':12, 'runId':51, 'preset':60},
                    {'seq':12, 'sample':13, 'runId':52, 'preset':60},
                    {'seq':13, 'sample':14, 'runId':53, 'preset':60},
                    {'seq':14, 'sample':15, 'runId':54, 'preset':60},
                    {'seq':15, 'sample':16, 'runId':55, 'preset':60},
                    {'seq':16, 'sample':17, 'runId':56, 'preset':60},
                    {'seq':17, 'sample':18, 'runId':57, 'preset':60},
                    {'seq':18, 'sample':19, 'runId':58, 'preset':60},
                    {'seq':19, 'sample':20, 'runId':59, 'preset':60},
                )
            },
        )
    },
    {
        'type':'sampleEnv', 'target':'0-dummy_motor', 'setting':1, 'contents':(
            {
                'type':'config', 'target':'0-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':1, 'runId':60, 'preset':60},
                    {'seq':1, 'sample':2, 'runId':61, 'preset':60},
                    {'seq':2, 'sample':3, 'runId':62, 'preset':60},
                    {'seq':3, 'sample':4, 'runId':63, 'preset':60},
                    {'seq':4, 'sample':5, 'runId':64, 'preset':60},
                    {'seq':5, 'sample':6, 'runId':65, 'preset':60},
                    {'seq':6, 'sample':7, 'runId':66, 'preset':60},
                    {'seq':7, 'sample':8, 'runId':67, 'preset':60},
                    {'seq':8, 'sample':9, 'runId':68, 'preset':60},
                    {'seq':9, 'sample':10, 'runId':69, 'preset':60},
                    {'seq':10, 'sample':11, 'runId':70, 'preset':60},
                    {'seq':11, 'sample':12, 'runId':71, 'preset':60},
                    {'seq':12, 'sample':13, 'runId':72, 'preset':60},
                    {'seq':13, 'sample':14, 'runId':73, 'preset':60},
                    {'seq':14, 'sample':15, 'runId':74, 'preset':60},
                    {'seq':15, 'sample':16, 'runId':75, 'preset':60},
                    {'seq':16, 'sample':17, 'runId':76, 'preset':60},
                    {'seq':17, 'sample':18, 'runId':77, 'preset':60},
                    {'seq':18, 'sample':19, 'runId':78, 'preset':60},
                    {'seq':19, 'sample':20, 'runId':79, 'preset':60},
                )
            },
            {
                'type':'config', 'target':'1-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':1, 'runId':80, 'preset':60},
                    {'seq':1, 'sample':2, 'runId':81, 'preset':60},
                    {'seq':2, 'sample':3, 'runId':82, 'preset':60},
                    {'seq':3, 'sample':4, 'runId':83, 'preset':60},
                    {'seq':4, 'sample':5, 'runId':84, 'preset':60},
                    {'seq':5, 'sample':6, 'runId':85, 'preset':60},
                    {'seq':6, 'sample':7, 'runId':86, 'preset':60},
                    {'seq':7, 'sample':8, 'runId':87, 'preset':60},
                    {'seq':8, 'sample':9, 'runId':88, 'preset':60},
                    {'seq':9, 'sample':10, 'runId':89, 'preset':60},
                    {'seq':10, 'sample':11, 'runId':90, 'preset':60},
                    {'seq':11, 'sample':12, 'runId':91, 'preset':60},
                    {'seq':12, 'sample':13, 'runId':92, 'preset':60},
                    {'seq':13, 'sample':14, 'runId':93, 'preset':60},
                    {'seq':14, 'sample':15, 'runId':94, 'preset':60},
                    {'seq':15, 'sample':16, 'runId':95, 'preset':60},
                    {'seq':16, 'sample':17, 'runId':96, 'preset':60},
                    {'seq':17, 'sample':18, 'runId':97, 'preset':60},
                    {'seq':18, 'sample':19, 'runId':98, 'preset':60},
                    {'seq':19, 'sample':20, 'runId':99, 'preset':60},
                )
            },
            {
                'type':'config', 'target':'2-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':1, 'runId':100, 'preset':60},
                    {'seq':1, 'sample':2, 'runId':101, 'preset':60},
                    {'seq':2, 'sample':3, 'runId':102, 'preset':60},
                    {'seq':3, 'sample':4, 'runId':103, 'preset':60},
                    {'seq':4, 'sample':5, 'runId':104, 'preset':60},
                    {'seq':5, 'sample':6, 'runId':105, 'preset':60},
                    {'seq':6, 'sample':7, 'runId':106, 'preset':60},
                    {'seq':7, 'sample':8, 'runId':107, 'preset':60},
                    {'seq':8, 'sample':9, 'runId':108, 'preset':60},
                    {'seq':9, 'sample':10, 'runId':109, 'preset':60},
                    {'seq':10, 'sample':11, 'runId':110, 'preset':60},
                    {'seq':11, 'sample':12, 'runId':111, 'preset':60},
                    {'seq':12, 'sample':13, 'runId':112, 'preset':60},
                    {'seq':13, 'sample':14, 'runId':113, 'preset':60},
                    {'seq':14, 'sample':15, 'runId':114, 'preset':60},
                    {'seq':15, 'sample':16, 'runId':115, 'preset':60},
                    {'seq':16, 'sample':17, 'runId':116, 'preset':60},
                    {'seq':17, 'sample':18, 'runId':117, 'preset':60},
                    {'seq':18, 'sample':19, 'runId':118, 'preset':60},
                    {'seq':19, 'sample':20, 'runId':119, 'preset':60},
                )
            },
        )
    },
    {
        'type':'sampleEnv', 'target':'0-dummy_motor', 'setting':2, 'contents':(
            {
                'type':'config', 'target':'0-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':1, 'runId':120, 'preset':60},
                    {'seq':1, 'sample':2, 'runId':121, 'preset':60},
                    {'seq':2, 'sample':3, 'runId':122, 'preset':60},
                    {'seq':3, 'sample':4, 'runId':123, 'preset':60},
                    {'seq':4, 'sample':5, 'runId':124, 'preset':60},
                    {'seq':5, 'sample':6, 'runId':125, 'preset':60},
                    {'seq':6, 'sample':7, 'runId':126, 'preset':60},
                    {'seq':7, 'sample':8, 'runId':127, 'preset':60},
                    {'seq':8, 'sample':9, 'runId':128, 'preset':60},
                    {'seq':9, 'sample':10, 'runId':129, 'preset':60},
                    {'seq':10, 'sample':11, 'runId':130, 'preset':60},
                    {'seq':11, 'sample':12, 'runId':131, 'preset':60},
                    {'seq':12, 'sample':13, 'runId':132, 'preset':60},
                    {'seq':13, 'sample':14, 'runId':133, 'preset':60},
                    {'seq':14, 'sample':15, 'runId':134, 'preset':60},
                    {'seq':15, 'sample':16, 'runId':135, 'preset':60},
                    {'seq':16, 'sample':17, 'runId':136, 'preset':60},
                    {'seq':17, 'sample':18, 'runId':137, 'preset':60},
                    {'seq':18, 'sample':19, 'runId':138, 'preset':60},
                    {'seq':19, 'sample':20, 'runId':139, 'preset':60},
                )
            },
            {
                'type':'config', 'target':'1-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':1, 'runId':140, 'preset':60},
                    {'seq':1, 'sample':2, 'runId':141, 'preset':60},
                    {'seq':2, 'sample':3, 'runId':142, 'preset':60},
                    {'seq':3, 'sample':4, 'runId':143, 'preset':60},
                    {'seq':4, 'sample':5, 'runId':144, 'preset':60},
                    {'seq':5, 'sample':6, 'runId':145, 'preset':60},
                    {'seq':6, 'sample':7, 'runId':146, 'preset':60},
                    {'seq':7, 'sample':8, 'runId':147, 'preset':60},
                    {'seq':8, 'sample':9, 'runId':148, 'preset':60},
                    {'seq':9, 'sample':10, 'runId':149, 'preset':60},
                    {'seq':10, 'sample':11, 'runId':150, 'preset':60},
                    {'seq':11, 'sample':12, 'runId':151, 'preset':60},
                    {'seq':12, 'sample':13, 'runId':152, 'preset':60},
                    {'seq':13, 'sample':14, 'runId':153, 'preset':60},
                    {'seq':14, 'sample':15, 'runId':154, 'preset':60},
                    {'seq':15, 'sample':16, 'runId':155, 'preset':60},
                    {'seq':16, 'sample':17, 'runId':156, 'preset':60},
                    {'seq':17, 'sample':18, 'runId':157, 'preset':60},
                    {'seq':18, 'sample':19, 'runId':158, 'preset':60},
                    {'seq':19, 'sample':20, 'runId':159, 'preset':60},
                )
            },
            {
                'type':'config', 'target':'2-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':1, 'runId':160, 'preset':60},
                    {'seq':1, 'sample':2, 'runId':161, 'preset':60},
                    {'seq':2, 'sample':3, 'runId':162, 'preset':60},
                    {'seq':3, 'sample':4, 'runId':163, 'preset':60},
                    {'seq':4, 'sample':5, 'runId':164, 'preset':60},
                    {'seq':5, 'sample':6, 'runId':165, 'preset':60},
                    {'seq':6, 'sample':7, 'runId':166, 'preset':60},
                    {'seq':7, 'sample':8, 'runId':167, 'preset':60},
                    {'seq':8, 'sample':9, 'runId':168, 'preset':60},
                    {'seq':9, 'sample':10, 'runId':169, 'preset':60},
                    {'seq':10, 'sample':11, 'runId':170, 'preset':60},
                    {'seq':11, 'sample':12, 'runId':171, 'preset':60},
                    {'seq':12, 'sample':13, 'runId':172, 'preset':60},
                    {'seq':13, 'sample':14, 'runId':173, 'preset':60},
                    {'seq':14, 'sample':15, 'runId':174, 'preset':60},
                    {'seq':15, 'sample':16, 'runId':175, 'preset':60},
                    {'seq':16, 'sample':17, 'runId':176, 'preset':60},
                    {'seq':17, 'sample':18, 'runId':177, 'preset':60},
                    {'seq':18, 'sample':19, 'runId':178, 'preset':60},
                    {'seq':19, 'sample':20, 'runId':179, 'preset':60},
                )
            },
        )
    },
    {
        'type':'sampleEnv', 'target':'0-dummy_motor', 'setting':3, 'contents':(
            {
                'type':'config', 'target':'0-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':1, 'runId':180, 'preset':60},
                    {'seq':1, 'sample':2, 'runId':181, 'preset':60},
                    {'seq':2, 'sample':3, 'runId':182, 'preset':60},
                    {'seq':3, 'sample':4, 'runId':183, 'preset':60},
                    {'seq':4, 'sample':5, 'runId':184, 'preset':60},
                    {'seq':5, 'sample':6, 'runId':185, 'preset':60},
                    {'seq':6, 'sample':7, 'runId':186, 'preset':60},
                    {'seq':7, 'sample':8, 'runId':187, 'preset':60},
                    {'seq':8, 'sample':9, 'runId':188, 'preset':60},
                    {'seq':9, 'sample':10, 'runId':189, 'preset':60},
                    {'seq':10, 'sample':11, 'runId':190, 'preset':60},
                    {'seq':11, 'sample':12, 'runId':191, 'preset':60},
                    {'seq':12, 'sample':13, 'runId':192, 'preset':60},
                    {'seq':13, 'sample':14, 'runId':193, 'preset':60},
                    {'seq':14, 'sample':15, 'runId':194, 'preset':60},
                    {'seq':15, 'sample':16, 'runId':195, 'preset':60},
                    {'seq':16, 'sample':17, 'runId':196, 'preset':60},
                    {'seq':17, 'sample':18, 'runId':197, 'preset':60},
                    {'seq':18, 'sample':19, 'runId':198, 'preset':60},
                    {'seq':19, 'sample':20, 'runId':199, 'preset':60},
                )
            },
            {
                'type':'config', 'target':'1-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':1, 'runId':200, 'preset':60},
                    {'seq':1, 'sample':2, 'runId':201, 'preset':60},
                    {'seq':2, 'sample':3, 'runId':202, 'preset':60},
                    {'seq':3, 'sample':4, 'runId':203, 'preset':60},
                    {'seq':4, 'sample':5, 'runId':204, 'preset':60},
                    {'seq':5, 'sample':6, 'runId':205, 'preset':60},
                    {'seq':6, 'sample':7, 'runId':206, 'preset':60},
                    {'seq':7, 'sample':8, 'runId':207, 'preset':60},
                    {'seq':8, 'sample':9, 'runId':208, 'preset':60},
                    {'seq':9, 'sample':10, 'runId':209, 'preset':60},
                    {'seq':10, 'sample':11, 'runId':210, 'preset':60},
                    {'seq':11, 'sample':12, 'runId':211, 'preset':60},
                    {'seq':12, 'sample':13, 'runId':212, 'preset':60},
                    {'seq':13, 'sample':14, 'runId':213, 'preset':60},
                    {'seq':14, 'sample':15, 'runId':214, 'preset':60},
                    {'seq':15, 'sample':16, 'runId':215, 'preset':60},
                    {'seq':16, 'sample':17, 'runId':216, 'preset':60},
                    {'seq':17, 'sample':18, 'runId':217, 'preset':60},
                    {'seq':18, 'sample':19, 'runId':218, 'preset':60},
                    {'seq':19, 'sample':20, 'runId':219, 'preset':60},
                )
            },
            {
                'type':'config', 'target':'2-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':1, 'runId':220, 'preset':60},
                    {'seq':1, 'sample':2, 'runId':221, 'preset':60},
                    {'seq':2, 'sample':3, 'runId':222, 'preset':60},
                    {'seq':3, 'sample':4, 'runId':223, 'preset':60},
                    {'seq':4, 'sample':5, 'runId':224, 'preset':60},
                    {'seq':5, 'sample':6, 'runId':225, 'preset':60},
                    {'seq':6, 'sample':7, 'runId':226, 'preset':60},
                    {'seq':7, 'sample':8, 'runId':227, 'preset':60},
                    {'seq':8, 'sample':9, 'runId':228, 'preset':60},
                    {'seq':9, 'sample':10, 'runId':229, 'preset':60},
                    {'seq':10, 'sample':11, 'runId':230, 'preset':60},
                    {'seq':11, 'sample':12, 'runId':231, 'preset':60},
                    {'seq':12, 'sample':13, 'runId':232, 'preset':60},
                    {'seq':13, 'sample':14, 'runId':233, 'preset':60},
                    {'seq':14, 'sample':15, 'runId':234, 'preset':60},
                    {'seq':15, 'sample':16, 'runId':235, 'preset':60},
                    {'seq':16, 'sample':17, 'runId':236, 'preset':60},
                    {'seq':17, 'sample':18, 'runId':237, 'preset':60},
                    {'seq':18, 'sample':19, 'runId':238, 'preset':60},
                    {'seq':19, 'sample':20, 'runId':239, 'preset':60},
                )
            },
        )
    },
    {
        'type':'sampleEnv', 'target':'0-dummy_motor', 'setting':4, 'contents':(
            {
                'type':'config', 'target':'0-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':1, 'runId':240, 'preset':60},
                    {'seq':1, 'sample':2, 'runId':241, 'preset':60},
                    {'seq':2, 'sample':3, 'runId':242, 'preset':60},
                    {'seq':3, 'sample':4, 'runId':243, 'preset':60},
                    {'seq':4, 'sample':5, 'runId':244, 'preset':60},
                    {'seq':5, 'sample':6, 'runId':245, 'preset':60},
                    {'seq':6, 'sample':7, 'runId':246, 'preset':60},
                    {'seq':7, 'sample':8, 'runId':247, 'preset':60},
                    {'seq':8, 'sample':9, 'runId':248, 'preset':60},
                    {'seq':9, 'sample':10, 'runId':249, 'preset':60},
                    {'seq':10, 'sample':11, 'runId':250, 'preset':60},
                    {'seq':11, 'sample':12, 'runId':251, 'preset':60},
                    {'seq':12, 'sample':13, 'runId':252, 'preset':60},
                    {'seq':13, 'sample':14, 'runId':253, 'preset':60},
                    {'seq':14, 'sample':15, 'runId':254, 'preset':60},
                    {'seq':15, 'sample':16, 'runId':255, 'preset':60},
                    {'seq':16, 'sample':17, 'runId':256, 'preset':60},
                    {'seq':17, 'sample':18, 'runId':257, 'preset':60},
                    {'seq':18, 'sample':19, 'runId':258, 'preset':60},
                    {'seq':19, 'sample':20, 'runId':259, 'preset':60},
                )
            },
            {
                'type':'config', 'target':'1-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':1, 'runId':260, 'preset':60},
                    {'seq':1, 'sample':2, 'runId':261, 'preset':60},
                    {'seq':2, 'sample':3, 'runId':262, 'preset':60},
                    {'seq':3, 'sample':4, 'runId':263, 'preset':60},
                    {'seq':4, 'sample':5, 'runId':264, 'preset':60},
                    {'seq':5, 'sample':6, 'runId':265, 'preset':60},
                    {'seq':6, 'sample':7, 'runId':266, 'preset':60},
                    {'seq':7, 'sample':8, 'runId':267, 'preset':60},
                    {'seq':8, 'sample':9, 'runId':268, 'preset':60},
                    {'seq':9, 'sample':10, 'runId':269, 'preset':60},
                    {'seq':10, 'sample':11, 'runId':270, 'preset':60},
                    {'seq':11, 'sample':12, 'runId':271, 'preset':60},
                    {'seq':12, 'sample':13, 'runId':272, 'preset':60},
                    {'seq':13, 'sample':14, 'runId':273, 'preset':60},
                    {'seq':14, 'sample':15, 'runId':274, 'preset':60},
                    {'seq':15, 'sample':16, 'runId':275, 'preset':60},
                    {'seq':16, 'sample':17, 'runId':276, 'preset':60},
                    {'seq':17, 'sample':18, 'runId':277, 'preset':60},
                    {'seq':18, 'sample':19, 'runId':278, 'preset':60},
                    {'seq':19, 'sample':20, 'runId':279, 'preset':60},
                )
            },
            {
                'type':'config', 'target':'2-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':1, 'runId':280, 'preset':60},
                    {'seq':1, 'sample':2, 'runId':281, 'preset':60},
                    {'seq':2, 'sample':3, 'runId':282, 'preset':60},
                    {'seq':3, 'sample':4, 'runId':283, 'preset':60},
                    {'seq':4, 'sample':5, 'runId':284, 'preset':60},
                    {'seq':5, 'sample':6, 'runId':285, 'preset':60},
                    {'seq':6, 'sample':7, 'runId':286, 'preset':60},
                    {'seq':7, 'sample':8, 'runId':287, 'preset':60},
                    {'seq':8, 'sample':9, 'runId':288, 'preset':60},
                    {'seq':9, 'sample':10, 'runId':289, 'preset':60},
                    {'seq':10, 'sample':11, 'runId':290, 'preset':60},
                    {'seq':11, 'sample':12, 'runId':291, 'preset':60},
                    {'seq':12, 'sample':13, 'runId':292, 'preset':60},
                    {'seq':13, 'sample':14, 'runId':293, 'preset':60},
                    {'seq':14, 'sample':15, 'runId':294, 'preset':60},
                    {'seq':15, 'sample':16, 'runId':295, 'preset':60},
                    {'seq':16, 'sample':17, 'runId':296, 'preset':60},
                    {'seq':17, 'sample':18, 'runId':297, 'preset':60},
                    {'seq':18, 'sample':19, 'runId':298, 'preset':60},
                    {'seq':19, 'sample':20, 'runId':299, 'preset':60},
                )
            },
        )
    },
)

###############################################################################
#
# Experiment logic
#
###############################################################################

if __name__ == '__main__':
    
    # Set up
    setup()
    
    # Set global settings
    workflow.configs = configs
    workflow.samples = samples
    workflow.sampleEnvironments = sampleEnvironments
    workflow.engineContext = __context__
    
    # Start looping through configurations
    try:
        workflow.runQuokkaScan(acqusitionEntries)
    except:
        logging.error('Exception occured. It will now go to clean up mode.')
        # Save result
        log('Saving intermediate result')
        sics.execute('newfile HISTOGRAM_XY')
        sics.execute('save')
        traceback.print_exc()
        print sys.exc_info()
    
    # Clean up
    cleanUp()

