#########################################
# Paladrium - a RPG Project             #
# https://github.com/Kanasaru/Paladrium #
# GPL 3.0 License                       #
#########################################

import pygame

# events
STARTGAME  = 1000
QUITGAME   = 1001

PLAYERDIED = 2000

class EventHandler():
    def __init__(self):
        self.e_startgame = pygame.event.Event(pygame.USEREVENT, e_type=STARTGAME)
        self.e_quitgame = pygame.event.Event(pygame.USEREVENT, e_type=QUITGAME)
        self.e_playerdied = pygame.event.Event(pygame.USEREVENT, e_type=PLAYERDIED)
        
    def get_events(self):
        self.events = pygame.event.get()
