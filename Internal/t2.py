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
    ## Drive attenuator to safe value
    #driveAtt(330)
    ##sics.drive('nvs_lambda', 5.0)
    ## Drive detector to short position
    #sics.set('/instrument/detector/detector_y/speed', 53)
    #driveDet(7200,300)
    ## Drive guide to g5 config
    #driveGuide(guideConfig.g5)
    ## Drive entrance aperture to 180 (for g5)
    #driveEntRotAp(180)
    ##set sample ap to 12.5 mm
    #sics.drive('apx', -98)
    ## Drive beamstops up
    #selBs(1)
    #sics.set('beamcenterx',38.53)
    #sics.set('beamcenterz', 95.98)
    pass

# Pre-transmission rountine for L1=L2=8m_offset_apx12.5_Aug2013 config
def driveToConfig0Transmission():
    ## Move the beamstop out
    #driveBsx(32.5, 100)
    ## Drive attenuator to 300
    #driveAtt(300)
    pass

# Pre-scattering rountine for L1=L2=8m_offset_apx12.5_Aug2013 config
def driveToConfig0Scattering():
    ## Drive attenuator to safe value
    #driveAtt(330)
    ## Move the beamstop in
    #driveBsx(32.5,0)
    #driveBsz(258.0)
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
        'startingAttenuation':30,
        'transmissionRoutine':driveToConfig0Transmission,
        'transmissionMode':scanMode.time,
        'transmissionPreset':30,
        'scatteringRoutine':driveToConfig0Scattering,
        'scatteringMode':scanMode.time,
    },
}

# Sample dictionary
samples = {
    3:{'position':3, 'name':'Thermocouple', 'type':'sample', 'description':'UNKNOWN', 'thickness':'0.0'},
    4:{'position':4, 'name':'MT beam', 'type':'empty_beam', 'description':'UNKNOWN', 'thickness':'0.0'},
    5:{'position':5, 'name':'MT cell', 'type':'empty_beam', 'description':'UNKNOWN', 'thickness':'1.0'},
    6:{'position':6, 'name':'Blocked beam', 'type':'sample', 'description':'UNKNOWN', 'thickness':'0.0'},
    7:{'position':7, 'name':'0% D2O BAMLET', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    8:{'position':8, 'name':'0% D2O buffer', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    9:{'position':9, 'name':'9.2% D2O BAMLET', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    10:{'position':10, 'name':'9.2% D2O BUFFER', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    11:{'position':11, 'name':'20% D2O BAMLET', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    12:{'position':12, 'name':'20% D2O BUFFER', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    13:{'position':13, 'name':'43.5% D2O BAMLET', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    14:{'position':14, 'name':'43.5% D2O BUFFER', 'type':'sample', 'description':'UNKNOWN', 'thickness':'1.0'},
    15:{'position':15, 'name':'60% D2O BAMLET', 'type':'sample', 'description':'UNKNOWN', 'thickness':'2.0'},
    16:{'position':16, 'name':'60% D2O BUFFER', 'type':'sample', 'description':'UNKNOWN', 'thickness':'2.0'},
    17:{'position':17, 'name':'80% D2O BAMLET', 'type':'sample', 'description':'UNKNOWN', 'thickness':'2.0'},
    18:{'position':18, 'name':'80% D2O BUFFER', 'type':'sample', 'description':'UNKNOWN', 'thickness':'2.0'},
    19:{'position':19, 'name':'100% D2O BAMLET', 'type':'sample', 'description':'UNKNOWN', 'thickness':'5.0'},
    20:{'position':20, 'name':'100% D2O BUFFER', 'type':'sample', 'description':'UNKNOWN', 'thickness':'5.0'},
}

# Sample environment dictionary
sampleEnvironments = {
    # Sample environment dummy_motor
    '0-dummy_motor':{
        'controller':'dummy_motor',
        0:{'preset':1.0, 'wait':30},
        1:{'preset':2.0, 'wait':30},
        2:{'preset':3.0, 'wait':30},
        3:{'preset':4.0, 'wait':30},
        4:{'preset':5.0, 'wait':30},
        5:{'preset':6.0, 'wait':30},
        6:{'preset':7.0, 'wait':30},
        7:{'preset':8.0, 'wait':30},
        8:{'preset':9.0, 'wait':30},
        9:{'preset':10.0, 'wait':30},
        10:{'preset':11.0, 'wait':30},
        11:{'preset':12.0, 'wait':30},
        12:{'preset':13.0, 'wait':30},
        13:{'preset':14.0, 'wait':30},
        14:{'preset':15.0, 'wait':30},
    },
}

# Acquisition dictionary
acqusitionEntries = (
    {
        'type':'sampleEnv', 'target':'0-dummy_motor', 'setting':0, 'contents':(
            {
                'type':'config', 'target':'0-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':3, 'runId':0, 'preset':30},
                    {'seq':1, 'sample':4, 'runId':1, 'preset':30},
                    {'seq':2, 'sample':5, 'runId':2, 'preset':30},
                    {'seq':3, 'sample':6, 'runId':3, 'preset':30},
                    {'seq':4, 'sample':7, 'runId':4, 'preset':30},
                    {'seq':5, 'sample':8, 'runId':5, 'preset':30},
                    {'seq':6, 'sample':9, 'runId':6, 'preset':30},
                    {'seq':7, 'sample':10, 'runId':7, 'preset':30},
                    {'seq':8, 'sample':11, 'runId':8, 'preset':30},
                    {'seq':9, 'sample':12, 'runId':9, 'preset':30},
                    {'seq':10, 'sample':13, 'runId':10, 'preset':30},
                    {'seq':11, 'sample':14, 'runId':11, 'preset':30},
                    {'seq':12, 'sample':15, 'runId':12, 'preset':30},
                    {'seq':13, 'sample':16, 'runId':13, 'preset':30},
                    {'seq':14, 'sample':17, 'runId':14, 'preset':30},
                    {'seq':15, 'sample':18, 'runId':15, 'preset':30},
                    {'seq':16, 'sample':19, 'runId':16, 'preset':30},
                    {'seq':17, 'sample':20, 'runId':17, 'preset':30},
                )
            },
        )
    },
    {
        'type':'sampleEnv', 'target':'0-dummy_motor', 'setting':1, 'contents':(
            {
                'type':'config', 'target':'0-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':3, 'runId':18, 'preset':30},
                    {'seq':1, 'sample':4, 'runId':19, 'preset':30},
                    {'seq':2, 'sample':5, 'runId':20, 'preset':30},
                    {'seq':3, 'sample':6, 'runId':21, 'preset':30},
                    {'seq':4, 'sample':7, 'runId':22, 'preset':30},
                    {'seq':5, 'sample':8, 'runId':23, 'preset':30},
                    {'seq':6, 'sample':9, 'runId':24, 'preset':30},
                    {'seq':7, 'sample':10, 'runId':25, 'preset':30},
                    {'seq':8, 'sample':11, 'runId':26, 'preset':30},
                    {'seq':9, 'sample':12, 'runId':27, 'preset':30},
                    {'seq':10, 'sample':13, 'runId':28, 'preset':30},
                    {'seq':11, 'sample':14, 'runId':29, 'preset':30},
                    {'seq':12, 'sample':15, 'runId':30, 'preset':30},
                    {'seq':13, 'sample':16, 'runId':31, 'preset':30},
                    {'seq':14, 'sample':17, 'runId':32, 'preset':30},
                    {'seq':15, 'sample':18, 'runId':33, 'preset':30},
                    {'seq':16, 'sample':19, 'runId':34, 'preset':30},
                    {'seq':17, 'sample':20, 'runId':35, 'preset':30},
                )
            },
        )
    },
    {
        'type':'sampleEnv', 'target':'0-dummy_motor', 'setting':2, 'contents':(
            {
                'type':'config', 'target':'0-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':3, 'runId':36, 'preset':30},
                    {'seq':1, 'sample':4, 'runId':37, 'preset':30},
                    {'seq':2, 'sample':5, 'runId':38, 'preset':30},
                    {'seq':3, 'sample':6, 'runId':39, 'preset':30},
                    {'seq':4, 'sample':7, 'runId':40, 'preset':30},
                    {'seq':5, 'sample':8, 'runId':41, 'preset':30},
                    {'seq':6, 'sample':9, 'runId':42, 'preset':30},
                    {'seq':7, 'sample':10, 'runId':43, 'preset':30},
                    {'seq':8, 'sample':11, 'runId':44, 'preset':30},
                    {'seq':9, 'sample':12, 'runId':45, 'preset':30},
                    {'seq':10, 'sample':13, 'runId':46, 'preset':30},
                    {'seq':11, 'sample':14, 'runId':47, 'preset':30},
                    {'seq':12, 'sample':15, 'runId':48, 'preset':30},
                    {'seq':13, 'sample':16, 'runId':49, 'preset':30},
                    {'seq':14, 'sample':17, 'runId':50, 'preset':30},
                    {'seq':15, 'sample':18, 'runId':51, 'preset':30},
                    {'seq':16, 'sample':19, 'runId':52, 'preset':30},
                    {'seq':17, 'sample':20, 'runId':53, 'preset':30},
                )
            },
        )
    },
    {
        'type':'sampleEnv', 'target':'0-dummy_motor', 'setting':3, 'contents':(
            {
                'type':'config', 'target':'0-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':3, 'runId':54, 'preset':30},
                    {'seq':1, 'sample':4, 'runId':55, 'preset':30},
                    {'seq':2, 'sample':5, 'runId':56, 'preset':30},
                    {'seq':3, 'sample':6, 'runId':57, 'preset':30},
                    {'seq':4, 'sample':7, 'runId':58, 'preset':30},
                    {'seq':5, 'sample':8, 'runId':59, 'preset':30},
                    {'seq':6, 'sample':9, 'runId':60, 'preset':30},
                    {'seq':7, 'sample':10, 'runId':61, 'preset':30},
                    {'seq':8, 'sample':11, 'runId':62, 'preset':30},
                    {'seq':9, 'sample':12, 'runId':63, 'preset':30},
                    {'seq':10, 'sample':13, 'runId':64, 'preset':30},
                    {'seq':11, 'sample':14, 'runId':65, 'preset':30},
                    {'seq':12, 'sample':15, 'runId':66, 'preset':30},
                    {'seq':13, 'sample':16, 'runId':67, 'preset':30},
                    {'seq':14, 'sample':17, 'runId':68, 'preset':30},
                    {'seq':15, 'sample':18, 'runId':69, 'preset':30},
                    {'seq':16, 'sample':19, 'runId':70, 'preset':30},
                    {'seq':17, 'sample':20, 'runId':71, 'preset':30},
                )
            },
        )
    },
    {
        'type':'sampleEnv', 'target':'0-dummy_motor', 'setting':4, 'contents':(
            {
                'type':'config', 'target':'0-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':3, 'runId':72, 'preset':30},
                    {'seq':1, 'sample':4, 'runId':73, 'preset':30},
                    {'seq':2, 'sample':5, 'runId':74, 'preset':30},
                    {'seq':3, 'sample':6, 'runId':75, 'preset':30},
                    {'seq':4, 'sample':7, 'runId':76, 'preset':30},
                    {'seq':5, 'sample':8, 'runId':77, 'preset':30},
                    {'seq':6, 'sample':9, 'runId':78, 'preset':30},
                    {'seq':7, 'sample':10, 'runId':79, 'preset':30},
                    {'seq':8, 'sample':11, 'runId':80, 'preset':30},
                    {'seq':9, 'sample':12, 'runId':81, 'preset':30},
                    {'seq':10, 'sample':13, 'runId':82, 'preset':30},
                    {'seq':11, 'sample':14, 'runId':83, 'preset':30},
                    {'seq':12, 'sample':15, 'runId':84, 'preset':30},
                    {'seq':13, 'sample':16, 'runId':85, 'preset':30},
                    {'seq':14, 'sample':17, 'runId':86, 'preset':30},
                    {'seq':15, 'sample':18, 'runId':87, 'preset':30},
                    {'seq':16, 'sample':19, 'runId':88, 'preset':30},
                    {'seq':17, 'sample':20, 'runId':89, 'preset':30},
                )
            },
        )
    },
    {
        'type':'sampleEnv', 'target':'0-dummy_motor', 'setting':5, 'contents':(
            {
                'type':'config', 'target':'0-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':3, 'runId':90, 'preset':30},
                    {'seq':1, 'sample':4, 'runId':91, 'preset':30},
                    {'seq':2, 'sample':5, 'runId':92, 'preset':30},
                    {'seq':3, 'sample':6, 'runId':93, 'preset':30},
                    {'seq':4, 'sample':7, 'runId':94, 'preset':30},
                    {'seq':5, 'sample':8, 'runId':95, 'preset':30},
                    {'seq':6, 'sample':9, 'runId':96, 'preset':30},
                    {'seq':7, 'sample':10, 'runId':97, 'preset':30},
                    {'seq':8, 'sample':11, 'runId':98, 'preset':30},
                    {'seq':9, 'sample':12, 'runId':99, 'preset':30},
                    {'seq':10, 'sample':13, 'runId':100, 'preset':30},
                    {'seq':11, 'sample':14, 'runId':101, 'preset':30},
                    {'seq':12, 'sample':15, 'runId':102, 'preset':30},
                    {'seq':13, 'sample':16, 'runId':103, 'preset':30},
                    {'seq':14, 'sample':17, 'runId':104, 'preset':30},
                    {'seq':15, 'sample':18, 'runId':105, 'preset':30},
                    {'seq':16, 'sample':19, 'runId':106, 'preset':30},
                    {'seq':17, 'sample':20, 'runId':107, 'preset':30},
                )
            },
        )
    },
    {
        'type':'sampleEnv', 'target':'0-dummy_motor', 'setting':6, 'contents':(
            {
                'type':'config', 'target':'0-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':3, 'runId':108, 'preset':30},
                    {'seq':1, 'sample':4, 'runId':109, 'preset':30},
                    {'seq':2, 'sample':5, 'runId':110, 'preset':30},
                    {'seq':3, 'sample':6, 'runId':111, 'preset':30},
                    {'seq':4, 'sample':7, 'runId':112, 'preset':30},
                    {'seq':5, 'sample':8, 'runId':113, 'preset':30},
                    {'seq':6, 'sample':9, 'runId':114, 'preset':30},
                    {'seq':7, 'sample':10, 'runId':115, 'preset':30},
                    {'seq':8, 'sample':11, 'runId':116, 'preset':30},
                    {'seq':9, 'sample':12, 'runId':117, 'preset':30},
                    {'seq':10, 'sample':13, 'runId':118, 'preset':30},
                    {'seq':11, 'sample':14, 'runId':119, 'preset':30},
                    {'seq':12, 'sample':15, 'runId':120, 'preset':7600},
                    {'seq':13, 'sample':16, 'runId':121, 'preset':7200},
                    {'seq':14, 'sample':17, 'runId':122, 'preset':7200},
                    {'seq':15, 'sample':18, 'runId':123, 'preset':7200},
                    {'seq':16, 'sample':19, 'runId':124, 'preset':7200},
                    {'seq':17, 'sample':20, 'runId':125, 'preset':7200},
                )
            },
        )
    },
    {
        'type':'sampleEnv', 'target':'0-dummy_motor', 'setting':7, 'contents':(
            {
                'type':'config', 'target':'0-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':3, 'runId':126, 'preset':30},
                    {'seq':1, 'sample':4, 'runId':127, 'preset':30},
                    {'seq':2, 'sample':5, 'runId':128, 'preset':30},
                    {'seq':3, 'sample':6, 'runId':129, 'preset':30},
                    {'seq':4, 'sample':7, 'runId':130, 'preset':30},
                    {'seq':5, 'sample':8, 'runId':131, 'preset':30},
                    {'seq':6, 'sample':9, 'runId':132, 'preset':30},
                    {'seq':7, 'sample':10, 'runId':133, 'preset':30},
                    {'seq':8, 'sample':11, 'runId':134, 'preset':30},
                    {'seq':9, 'sample':12, 'runId':135, 'preset':30},
                    {'seq':10, 'sample':13, 'runId':136, 'preset':30},
                    {'seq':11, 'sample':14, 'runId':137, 'preset':30},
                    {'seq':12, 'sample':15, 'runId':138, 'preset':30},
                    {'seq':13, 'sample':16, 'runId':139, 'preset':30},
                    {'seq':14, 'sample':17, 'runId':140, 'preset':30},
                    {'seq':15, 'sample':18, 'runId':141, 'preset':30},
                    {'seq':16, 'sample':19, 'runId':142, 'preset':30},
                    {'seq':17, 'sample':20, 'runId':143, 'preset':30},
                )
            },
        )
    },
    {
        'type':'sampleEnv', 'target':'0-dummy_motor', 'setting':8, 'contents':(
            {
                'type':'config', 'target':'0-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':3, 'runId':144, 'preset':30},
                    {'seq':1, 'sample':4, 'runId':145, 'preset':30},
                    {'seq':2, 'sample':5, 'runId':146, 'preset':30},
                    {'seq':3, 'sample':6, 'runId':147, 'preset':30},
                    {'seq':4, 'sample':7, 'runId':148, 'preset':30},
                    {'seq':5, 'sample':8, 'runId':149, 'preset':30},
                    {'seq':6, 'sample':9, 'runId':150, 'preset':30},
                    {'seq':7, 'sample':10, 'runId':151, 'preset':30},
                    {'seq':8, 'sample':11, 'runId':152, 'preset':30},
                    {'seq':9, 'sample':12, 'runId':153, 'preset':30},
                    {'seq':10, 'sample':13, 'runId':154, 'preset':30},
                    {'seq':11, 'sample':14, 'runId':155, 'preset':30},
                    {'seq':12, 'sample':15, 'runId':156, 'preset':30},
                    {'seq':13, 'sample':16, 'runId':157, 'preset':30},
                    {'seq':14, 'sample':17, 'runId':158, 'preset':30},
                    {'seq':15, 'sample':18, 'runId':159, 'preset':30},
                    {'seq':16, 'sample':19, 'runId':160, 'preset':30},
                    {'seq':17, 'sample':20, 'runId':161, 'preset':30},
                )
            },
        )
    },
    {
        'type':'sampleEnv', 'target':'0-dummy_motor', 'setting':9, 'contents':(
            {
                'type':'config', 'target':'0-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':3, 'runId':162, 'preset':30},
                    {'seq':1, 'sample':4, 'runId':163, 'preset':30},
                    {'seq':2, 'sample':5, 'runId':164, 'preset':30},
                    {'seq':3, 'sample':6, 'runId':165, 'preset':30},
                    {'seq':4, 'sample':7, 'runId':166, 'preset':30},
                    {'seq':5, 'sample':8, 'runId':167, 'preset':30},
                    {'seq':6, 'sample':9, 'runId':168, 'preset':30},
                    {'seq':7, 'sample':10, 'runId':169, 'preset':30},
                    {'seq':8, 'sample':11, 'runId':170, 'preset':30},
                    {'seq':9, 'sample':12, 'runId':171, 'preset':30},
                    {'seq':10, 'sample':13, 'runId':172, 'preset':30},
                    {'seq':11, 'sample':14, 'runId':173, 'preset':30},
                    {'seq':12, 'sample':15, 'runId':174, 'preset':30},
                    {'seq':13, 'sample':16, 'runId':175, 'preset':30},
                    {'seq':14, 'sample':17, 'runId':176, 'preset':30},
                    {'seq':15, 'sample':18, 'runId':177, 'preset':30},
                    {'seq':16, 'sample':19, 'runId':178, 'preset':30},
                    {'seq':17, 'sample':20, 'runId':179, 'preset':30},
                )
            },
        )
    },
    {
        'type':'sampleEnv', 'target':'0-dummy_motor', 'setting':10, 'contents':(
            {
                'type':'config', 'target':'0-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':3, 'runId':180, 'preset':30},
                    {'seq':1, 'sample':4, 'runId':181, 'preset':30},
                    {'seq':2, 'sample':5, 'runId':182, 'preset':30},
                    {'seq':3, 'sample':6, 'runId':183, 'preset':30},
                    {'seq':4, 'sample':7, 'runId':184, 'preset':30},
                    {'seq':5, 'sample':8, 'runId':185, 'preset':30},
                    {'seq':6, 'sample':9, 'runId':186, 'preset':30},
                    {'seq':7, 'sample':10, 'runId':187, 'preset':30},
                    {'seq':8, 'sample':11, 'runId':188, 'preset':30},
                    {'seq':9, 'sample':12, 'runId':189, 'preset':30},
                    {'seq':10, 'sample':13, 'runId':190, 'preset':30},
                    {'seq':11, 'sample':14, 'runId':191, 'preset':30},
                    {'seq':12, 'sample':15, 'runId':192, 'preset':30},
                    {'seq':13, 'sample':16, 'runId':193, 'preset':30},
                    {'seq':14, 'sample':17, 'runId':194, 'preset':30},
                    {'seq':15, 'sample':18, 'runId':195, 'preset':30},
                    {'seq':16, 'sample':19, 'runId':196, 'preset':30},
                    {'seq':17, 'sample':20, 'runId':197, 'preset':30},
                )
            },
        )
    },
    {
        'type':'sampleEnv', 'target':'0-dummy_motor', 'setting':11, 'contents':(
            {
                'type':'config', 'target':'0-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':3, 'runId':198, 'preset':30},
                    {'seq':1, 'sample':4, 'runId':199, 'preset':30},
                    {'seq':2, 'sample':5, 'runId':200, 'preset':30},
                    {'seq':3, 'sample':6, 'runId':201, 'preset':30},
                    {'seq':4, 'sample':7, 'runId':202, 'preset':30},
                    {'seq':5, 'sample':8, 'runId':203, 'preset':30},
                    {'seq':6, 'sample':9, 'runId':204, 'preset':30},
                    {'seq':7, 'sample':10, 'runId':205, 'preset':30},
                    {'seq':8, 'sample':11, 'runId':206, 'preset':30},
                    {'seq':9, 'sample':12, 'runId':207, 'preset':30},
                    {'seq':10, 'sample':13, 'runId':208, 'preset':30},
                    {'seq':11, 'sample':14, 'runId':209, 'preset':30},
                    {'seq':12, 'sample':15, 'runId':210, 'preset':30},
                    {'seq':13, 'sample':16, 'runId':211, 'preset':30},
                    {'seq':14, 'sample':17, 'runId':212, 'preset':30},
                    {'seq':15, 'sample':18, 'runId':213, 'preset':30},
                    {'seq':16, 'sample':19, 'runId':214, 'preset':30},
                    {'seq':17, 'sample':20, 'runId':215, 'preset':30},
                )
            },
        )
    },
    {
        'type':'sampleEnv', 'target':'0-dummy_motor', 'setting':12, 'contents':(
            {
                'type':'config', 'target':'0-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':3, 'runId':216, 'preset':30},
                    {'seq':1, 'sample':4, 'runId':217, 'preset':30},
                    {'seq':2, 'sample':5, 'runId':218, 'preset':30},
                    {'seq':3, 'sample':6, 'runId':219, 'preset':30},
                    {'seq':4, 'sample':7, 'runId':220, 'preset':30},
                    {'seq':5, 'sample':8, 'runId':221, 'preset':30},
                    {'seq':6, 'sample':9, 'runId':222, 'preset':30},
                    {'seq':7, 'sample':10, 'runId':223, 'preset':30},
                    {'seq':8, 'sample':11, 'runId':224, 'preset':30},
                    {'seq':9, 'sample':12, 'runId':225, 'preset':30},
                    {'seq':10, 'sample':13, 'runId':226, 'preset':30},
                    {'seq':11, 'sample':14, 'runId':227, 'preset':30},
                    {'seq':12, 'sample':15, 'runId':228, 'preset':30},
                    {'seq':13, 'sample':16, 'runId':229, 'preset':30},
                    {'seq':14, 'sample':17, 'runId':230, 'preset':30},
                    {'seq':15, 'sample':18, 'runId':231, 'preset':30},
                    {'seq':16, 'sample':19, 'runId':232, 'preset':30},
                    {'seq':17, 'sample':20, 'runId':233, 'preset':30},
                )
            },
        )
    },
    {
        'type':'sampleEnv', 'target':'0-dummy_motor', 'setting':13, 'contents':(
            {
                'type':'config', 'target':'0-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':3, 'runId':234, 'preset':30},
                    {'seq':1, 'sample':4, 'runId':235, 'preset':30},
                    {'seq':2, 'sample':5, 'runId':236, 'preset':30},
                    {'seq':3, 'sample':6, 'runId':237, 'preset':30},
                    {'seq':4, 'sample':7, 'runId':238, 'preset':30},
                    {'seq':5, 'sample':8, 'runId':239, 'preset':30},
                    {'seq':6, 'sample':9, 'runId':240, 'preset':30},
                    {'seq':7, 'sample':10, 'runId':241, 'preset':30},
                    {'seq':8, 'sample':11, 'runId':242, 'preset':30},
                    {'seq':9, 'sample':12, 'runId':243, 'preset':30},
                    {'seq':10, 'sample':13, 'runId':244, 'preset':30},
                    {'seq':11, 'sample':14, 'runId':245, 'preset':30},
                    {'seq':12, 'sample':15, 'runId':246, 'preset':30},
                    {'seq':13, 'sample':16, 'runId':247, 'preset':30},
                    {'seq':14, 'sample':17, 'runId':248, 'preset':30},
                    {'seq':15, 'sample':18, 'runId':249, 'preset':30},
                    {'seq':16, 'sample':19, 'runId':250, 'preset':30},
                    {'seq':17, 'sample':20, 'runId':251, 'preset':30},
                )
            },
        )
    },
    {
        'type':'sampleEnv', 'target':'0-dummy_motor', 'setting':14, 'contents':(
            {
                'type':'config', 'target':'0-L1=L2=8m_offset_apx12.5_Aug2013', 'contents':(
                    {'seq':0, 'sample':3, 'runId':252, 'preset':30},
                    {'seq':1, 'sample':4, 'runId':253, 'preset':30},
                    {'seq':2, 'sample':5, 'runId':254, 'preset':30},
                    {'seq':3, 'sample':6, 'runId':255, 'preset':30},
                    {'seq':4, 'sample':7, 'runId':256, 'preset':30},
                    {'seq':5, 'sample':8, 'runId':257, 'preset':30},
                    {'seq':6, 'sample':9, 'runId':258, 'preset':30},
                    {'seq':7, 'sample':10, 'runId':259, 'preset':30},
                    {'seq':8, 'sample':11, 'runId':260, 'preset':30},
                    {'seq':9, 'sample':12, 'runId':261, 'preset':30},
                    {'seq':10, 'sample':13, 'runId':262, 'preset':30},
                    {'seq':11, 'sample':14, 'runId':263, 'preset':30},
                    {'seq':12, 'sample':15, 'runId':264, 'preset':30},
                    {'seq':13, 'sample':16, 'runId':265, 'preset':30},
                    {'seq':14, 'sample':17, 'runId':266, 'preset':30},
                    {'seq':15, 'sample':18, 'runId':267, 'preset':30},
                    {'seq':16, 'sample':19, 'runId':268, 'preset':30},
                    {'seq':17, 'sample':20, 'runId':269, 'preset':30},
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

