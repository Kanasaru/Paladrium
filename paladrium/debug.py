#########################################
# Paladrium - a RPG Project             #
# https://github.com/Kanasaru/Paladrium #
# GPL 3.0 License                       #
#########################################

### IMPORTS & INITIALISATON


### CONSTANTS

QUIET  = 0
SILENT = 1
LOUD   = 2

### GLOBALS

__DEBUGMODE = QUIET

### CLASSES & FUNCTIONS

##
# Class: Debug()
# Parent: none
##
class Debug():
    
    def __init__(self, mode=SILENT):
        
        global DEBUGMODE
        
        DEBUGMODE = mode
        
        if DEBUGMODE == QUIET:
            print("\nDebugging is set to QUIET:\nNothing will be printed in console, except of Python and PyGame general errors.")
        elif DEBUGMODE == SILENT:
            print("\nDebugging is set to SILENT:\nEverything will be printed in console.")
        elif DEBUGMODE == LOUD:
            print("\nDebugging is set to LOUD:\nEverything will be printed in console and a debugbar will be visible in the PyGame display.")
        
    
    def msg(message):
        
        global DEBUGMODE
        
        if DEBUGMODE == SILENT or DEBUGMODE == LOUD:
            print(message)
            