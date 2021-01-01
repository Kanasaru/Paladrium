#########################################
# Paladrium - a RPG Project             #
# https://github.com/Kanasaru/Paladrium #
# GPL 3.0 License                       #
#########################################

### IMPORTS & INITIALISATON

import pygame


### CONSTANTS

# Paladrium events
STARTGAME  = 1000
QUITGAME   = 1001
LOADGAME   = 1002
RESOLUTION = 1003
NEWTITLE   = 1004


### CLASSES & FUNCTIONS

##
# Class: Event()
# Parent: none
##
class Event():
    
    ##
    # Method: __init__
    # Class: Event()
    # @param: (int) code
    # @param: (mixed) data
    # @return: none
    ##
    def __init__(self, code, data):
        
        self.code = code
        self.data = data
        
    ##
    # Method: __str__
    # Class: Event()
    # @param: none
    # @return: (str) printstrings
    ##
    def __str__(self):
        
        # build up custom string for print(self) with event code
        printstring = "Event [" + str(self.code) + "]"
        
        # plus extra information for some event codes
        if self.code == NEWTITLE:
            printstring += " [NEWTITLE]: "
            
        # and adding given event data
        printstring += str(self.data)
        
        return printstring
        