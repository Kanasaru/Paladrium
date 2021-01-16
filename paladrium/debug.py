#########################################
# Paladrium - a RPG Project             #
# https://github.com/Kanasaru/Paladrium #
# GPL 3.0 License                       #
#########################################

### IMPORTS & INITIALISATON

from . import forms
import pygame

### CONSTANTS

QUIET  = 0
SILENT = 1
LOUD   = 2

### GLOBALS

__DEBUGMODE = SILENT

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
        
        self.text = "Let's test the debug text"
        
    def create_surface(self):
        
        infoObject = pygame.display.Info()
        
        self.surface = forms.Title((infoObject.current_w, infoObject.current_h), (255, 255, 255), (0, 0), 60)
        
        attr = {
            "pos-x":            5,
            "pos-y":            0,
            "text":             self.text,
            "text-font":        "assets/RobotoMono-VariableFont_wght.ttf",
            "text-size":        16,
            "text-color":       (255, 255, 255)
            }
        self.surface.add(forms.Text(attr))
        
    def handle_event(self, event):
        return
            
    def run_logic(self):
        self.text = "Hm...nothing for the logic part"
        
    def render(self):
        self.create_surface()
        self.surface.render()
        
    def toggle(self):
        global DEBUGMODE
        
        if DEBUGMODE == QUIET:
            DEBUGMODE = SILENT
            print("\nDebugging is set to SILENT:\nEverything will be printed in console.")
        elif DEBUGMODE == SILENT:
            DEBUGMODE = LOUD
            print("\nDebugging is set to LOUD:\nEverything will be printed in console and a debugbar will be visible in the PyGame display.")
        else:
            DEBUGMODE = QUIET
            print("\nDebugging is set to QUIET:\nNothing will be printed in console, except of Python and PyGame general errors.")
        
    def msg(message):
        
        global DEBUGMODE
        
        if DEBUGMODE == SILENT or DEBUGMODE == LOUD:
            print(message)
            
    def is_loud():
        
        global DEBUGMODE
        
        if DEBUGMODE == LOUD:
            return True
            
        return False
            