#########################################
# Paladrium - a RPG Project             #
# https://github.com/Kanasaru/Paladrium #
# GPL 3.0 License                       #
#########################################

import pygame

# events
MAINMENU   = 1000
NEWGAME    = 1001
STARTGAME  = 1002
QUITGAME   = 1003

PLAYERDIED = 2000

class EventHandler():
    def __init__(self):
        self.e_mainmenu = pygame.event.Event(pygame.USEREVENT, e_type=MAINMENU)
        self.e_newgame = pygame.event.Event(pygame.USEREVENT, e_type=NEWGAME)
        self.e_startgame = pygame.event.Event(pygame.USEREVENT, e_type=STARTGAME)
        self.e_quitgame = pygame.event.Event(pygame.USEREVENT, e_type=QUITGAME)
        self.e_playerdied = pygame.event.Event(pygame.USEREVENT, e_type=PLAYERDIED)
        
    def get_events(self):
        self.events = pygame.event.get()
