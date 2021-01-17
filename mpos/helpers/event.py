#########################################
# MPoS - just a library for development #
#########################################

### IMPORTS & INITIALISATON

from mpos.helpers.logger import log

### CONSTANTS

### GLOBALS

### CLASSES & FUNCTIONS

class Event():
    
    def __init__(self, code, data):
        
        self.code = code
        self.data = data
        
    def __str__(self):
        
        # build up custom string for print(self) with event code
        printstring = "Event [" + str(self.code) + "]"
            
        # and adding given event data
        printstring += str(self.data)
        
        return printstring
