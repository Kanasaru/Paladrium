#########################################
# Paladrium - a RPG Project             #
# https://github.com/Kanasaru/Paladrium #
# GPL 3.0 License                       #
#########################################

import pygame

class EventHandler():
    
    MAINMENU   = 1000
    NEWGAME    = 1001
    STARTGAME  = 1002
    QUITGAME   = 1003

    def __init__(self):
        self.e_mainmenu = pygame.event.Event(pygame.USEREVENT, e_type=self.MAINMENU)
        self.e_newgame = pygame.event.Event(pygame.USEREVENT, e_type=self.NEWGAME)
        self.e_startgame = pygame.event.Event(pygame.USEREVENT, e_type=self.STARTGAME)
        self.e_quitgame = pygame.event.Event(pygame.USEREVENT, e_type=self.QUITGAME)
        
    def collect_events(self):
        self.events = pygame.event.get()

    def get_events(self):
        return self.events