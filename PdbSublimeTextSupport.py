import os
import os.path

from os.path import exists

COMMAND = 'subl'
COMMAND_ARGS = ' -b "%s:%d"'

def launch(self):
    frame, lineno = self.stack[self.curindex]
    filename = self.canonic(frame.f_code.co_filename)
    if exists(filename):
        command = (COMMAND + COMMAND_ARGS) % (filename, lineno)
        os.system(command)

def preloop(self):
    launch(self)

def precmd(self, line):
    launch(self)
    return line
