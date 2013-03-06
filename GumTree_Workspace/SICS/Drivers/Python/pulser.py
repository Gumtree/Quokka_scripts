from gumpy.commons import logger
from gumpy.commons import sics

def drive(preset):
    logger.log('Setting pulser voltage to ' + str(preset) + 'mV')
    sics.execute('setvolt ' + str(preset))