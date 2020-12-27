#########################################
# Paladrium - a RPG Project             #
# https://github.com/Kanasaru/Paladrium #
# GPL 3.0 License                       #
#########################################

### IMPORTS & INITIALISATON

import pygame

### CLASSES & FUNCTIONS

##
# Class: EventHandler()
# Parent: none
# Defines and handles all pygame.USEREVENTS
##

class EventHandler():
    
    # event codes
    MAINMENU   = 1000
    NEWGAME    = 1001
    STARTGAME  = 1002
    QUITGAME   = 1003

    ##
    # Method: __init__
    # Class: Settings()
    # @param: none
    # @return: none
    # Init all pygame.USEREVENTS
    ##
    def __init__(self):
        self.e_mainmenu = pygame.event.Event(pygame.USEREVENT, e_type=self.MAINMENU)
        self.e_newgame = pygame.event.Event(pygame.USEREVENT, e_type=self.NEWGAME)
        self.e_startgame = pygame.event.Event(pygame.USEREVENT, e_type=self.STARTGAME)
        self.e_quitgame = pygame.event.Event(pygame.USEREVENT, e_type=self.QUITGAME)

    ##
    # Method: collect_events
    # Class: Settings()
    # @param: none
    # @return: none
    # Grabs all raised events and store it
    ##
    def collect_events(self):
        # grab pygame events (empties queue)
        self.events = pygame.event.get()
    
    ##
    # Method: get_events
    # Class: Settings()
    # @param: none
    # @return: none
    # Returns all stored events
    ##
    def get_events(self):
        return self.events
