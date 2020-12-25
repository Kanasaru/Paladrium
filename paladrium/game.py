#########################################
# Paladrium - a RPG Project             #
# https://github.com/Kanasaru/Paladrium #
# GPL 3.0 License                       #
#########################################


### IMPORTS & INITIALISATON

# PyGame
import pygame
pygame.init()

# Paladrium packages
from . import constants
from . import surface
from . import title
from . import events


### CLASSES & FUNCTIONS

##
# Class: Game()
# Object holds every information of a running instance of Paladrium
# After inititializing and call start() it runs the gameloop.
##

class Game():
    
    def __init__(self, path):
        self.gamepath = path
        self.exit_game = False
        self.clock = pygame.time.Clock()
        
        self.eventhandler = events.EventHandler()
        
    def start(self):
        # create window and main title
        self.screen()
        
        # start the loop
        self.loop()
        
    def screen(self):
        # build main window
        self.screen = pygame.display.set_mode((constants.DISPLAYWIDTH, constants.DISPLAYHEIGHT))
        self.screen.fill(constants.BLACK)
        display_title = "Paladrium - v" + constants.VERSION + " by " + constants.AUTHOR
        pygame.display.set_caption(display_title)

        # build main title screen
        self.current_screen = title.MainTitle(self.screen, self.eventhandler)
        
    def loop(self):
        while not self.exit_game:
            
            # set framerate
            self.clock.tick(constants.FPS)
            
            # eventhandling
            self.eventhandler.get_events()
            
            self.current_screen.handle_events()
            
            for event in self.eventhandler.events:
                if event.type == pygame.QUIT:
                    self.exit_game = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        print("key LEFT pressed")
                    if event.key == pygame.K_RIGHT:
                        print("key RIGHT pressed")
                    if event.key == pygame.K_UP:
                        print("key UP pressed")
                    if event.key == pygame.K_DOWN:
                        print("key DOWN pressed")
     
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        print("key LEFT released")
                    if event.key == pygame.K_RIGHT:
                        print("key RIGHT released")
                    if event.key == pygame.K_UP:
                        print("key UP released")
                    if event.key == pygame.K_DOWN:
                        print("key DOWN released")
                        
                if event.type == pygame.USEREVENT:
                    if event.e_type == events.QUITGAME:
                        print("Userevent: QUITGAME")
                        self.exit_game = True
            
            # logic
            self.current_screen.run_logic()
            
            # rendering
            self.current_screen.render()
            
            pygame.display.flip()
               
        self.exit()
            
    def exit(self):
        print(self.eventhandler.events)
        pygame.quit()
