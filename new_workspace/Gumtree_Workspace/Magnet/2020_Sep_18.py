from gumpy.commons import sics
from bragg.quokka import quokka

_mode = quokka.ACQUISITION_MODE.time

def drive_to_config2():
    slog('run instrument to config 2')
    config.wavelength = 5
    config.wavelength_spread = 0.1
    config.det = 7200
    config.det_offset = 0
    config.srce = 180
    config.guide = 'g5'
    config.apx = -72
    config.bs = 2
    config.beamcenterx = 89.227
    config.beamcenterz = 95.9224
    config.drive()
    driveBsx(35,0)
    driveBsz(256)
    sics.drive('att', 0)
    
def drive_to_config1():
    slog('run instrument to config 1')
    config.wavelength = 7
    config.wavelength_spread = 0.1
    config.det = 7200
    config.det_offset = 0
    config.srce = 180
    config.guide = 'p1'
    config.bs = 2
    config.beamcenterx = 91.87
    config.beamcenterz = 95.57
    config.drive()
    driveBsx(38,0)
    driveBsz(258)
    sics.drive('att', 0)
    
def set_pol_on():
    slog('set polarisation on')
    sics.set('/instrument/flipper/set_flip_on', 1)
    time.sleep(45)
    
def set_pol_off():
    slog('set polarisation off')
    sics.set('/instrument/flipper/set_flip_on', 0)
    
def on_off_collection(temp, field, preset):
    slog('on and off collection for {}'.format(preset))
    sics.drive('tc1_temp0_setpoint', temp)
    sics.drive('ma1_magnet_setpoint', field)
    set_pol_on()
    quokka.scan(_mode, preset)
    slog('file saved at {}'.format(sics.get_base_filename()))
    set_pol_off()
    quokka.scan(_mode, preset)
    slog('file saved at {}'.format(sics.get_base_filename()))
    
def temp_ramp_collection(temp, preset):
    slog('drive temp to {}K, collect for {}'.format(temp, preset))
    set_pol_off()
    slog('drive temp')
    sics.run('tc1_temp0_setpoint', temp)
    slog('start collection')
    quokka.scan(_mode, preset)
    slog('file saved at {}'.format(sics.get_base_filename()))
    
def field_collection(field, preset):
    slog('drive field to {}, collect for {}'.format(field, preset))
    sics.drive('ma1_magnet_setpoint', field)
    if field == 0:
        quokka.scan(_mode, preset)
        slog('file saved at {}'.format(sics.get_base_filename()))
    else:
        set_pol_on()
        quokka.scan(_mode, preset)
        slog('file saved at {}'.format(sics.get_base_filename()))
        set_pol_off()
        quokka.scan(_mode, preset)
        slog('file saved at {}'.format(sics.get_base_filename()))
        
# config(1) is polarised
# config(2) is unpolarised

def run():
    drive_to_config1()
    on_off_collection(300, -1, 3600)
    
    drive_to_config2()
    temp_ramp_collection(200, 2.5*3600)
    
    drive_to_config1()
    on_off_collection(200, -1, 3600)
    
    drive_to_config2()
    temp_ramp_collection(150, 1.5*3600)
    
    drive_to_config1()
    on_off_collection(150, -1, 3600)
    
    drive_to_config2()
    temp_ramp_collection(100, 1.5*3600)
    
    drive_to_config1()
    on_off_collection(100, -1, 3600)
    
    drive_to_config2()
    temp_ramp_collection(20, 2.1*3600)
    
    drive_to_config1()
    on_off_collection(20, -1, 3600)
    
    drive_to_config2()
    temp_ramp_collection(5, 1.1*3600)
    
    drive_to_config1()
    on_off_collection(5, -1, 3600)
    
    drive_to_config2()
    field_collection(0, 1200)
    
    drive_to_config1()
    field_collection(-0.2, 3600)
    field_collection(-0.5, 3600)
    field_collection(-1, 3600)
    field_collection(-3, 3600)
    field_collection(-0.5, 3600)
    field_collection(-0.2, 3600)
    field_collection(-0.1, 3600)
    
    drive_to_config2()
    field_collection(0, 1200)
    field_collection(0.1, 1200)
    field_collection(0.2, 1200)
    field_collection(0.5, 1200)
    field_collection(1, 1200)
    field_collection(2, 1200)
    field_collection(3, 1200)
    field_collection(2, 1200)
    field_collection(1, 1200)
    field_collection(0.5, 1200)
    field_collection(0.2, 1200)
    field_collection(0.1, 1200)
    field_collection(0, 1200)
    
    drive_to_config1()
    field_collection(-0.1, 3600)
    field_collection(-0.2, 3600)
    field_collection(-0.5, 3600)
    field_collection(-1, 3600)
    field_collection(-2, 3600)
    field_collection(-3, 3600)
    
    drive_to_config2()
    field_collection(0, 1200)
    sics.drive('ma1_magnet_setpoint', -1.0)
    
    drive_to_config2()
    temp_ramp_collection(20, 1.1*3600)
    
    drive_to_config1()
    on_off_collection(20, -1, 3600)
    
    drive_to_config2()
    temp_ramp_collection(100, 2.1*3600)
    
    drive_to_config1()
    on_off_collection(100, -1, 3600)
    
    drive_to_config2()
    temp_ramp_collection(150, 1.5*3600)
    
    drive_to_config1()
    on_off_collection(150, -1, 3600)
    
    drive_to_config2()
    temp_ramp_collection(200, 1.5*3600)
    
    drive_to_config1()
    on_off_collection(200, -1, 3600)
    
    drive_to_config2()
    temp_ramp_collection(300, 2.5*3600)
    
    drive_to_config1()
    on_off_collection(300, -1, 3600)
    
#def test():
    #drive_to_config1()
    #on_off_collection(300, 0.1, 10)
    
    #drive_to_config2()
    #temp_ramp_collection(300, 120)
    
    #field_collection(0.2, 10)
    
#run()