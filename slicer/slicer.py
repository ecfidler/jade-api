'''
using slic3r cli
https://manual.slic3r.org/advanced/command-line
^ for .ini generation, find: "Export Config" (it is generated in the slicer command)


and subprocess
https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output

`slic3r --gcode MODELNAME --load config.ini`
'''

import subprocess

def slice_file(file_name):
    file_path = 'path/'
    cmd = ['slic3r', '--gcode', f'{file_path}{file_name}', '--load', 'config.ini']
    # subprocess.check_output(cmd, ) # I probably want to use subprocess.run