# Script control setup area
# script info
#__script__.title = 'Scan Guide'
#__script__.version = '1.0'

# Use below example to create parameters.
# The type can be string, int, float, bool, file.
guide_names = Par('string', 'ga,g1,g2,g3,g4,g5,g6,g7,g8,g9')
count_mode = Par('string', 'time', options=['time', 'count'])
count_preset = Par('float', 120)
att = Par('float', 270)

# Use below example to create a button
act1 = Act('act1_changed()', 'run scan') 
def act1_changed():
    guides = guide_names.value
    if len(guides) > 0:
        if count_mode.value == 'time':
            mode = 'time'
        else:
            mode = 'count'
        guideList = guides.split(',')
        
        config.clear()
        for g in guideList:
            slog('drive guide ' + g)
            config.guide = g
            config.drive()
            
            quokka.driveAtt(att.value)
            
            slog('scan ' + str(mode) + ' ' + str(count_preset.value))
            quokka.scan(mode, count_preset.value)
            slog('file saved at ' + sics.get_base_filename())
            
    
# Use below example to create a new Plot
# Plot4 = Plot(title = 'new plot')

# This function is called when pushing the Run button in the control UI.
def __run_script__(fns):
    act1_changed()
    
def __dispose__():
    global Plot1
    global Plot2
    global Plot3
    Plot1.clear()
    Plot2.clear()
    Plot3.clear()
