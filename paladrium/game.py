#########################################
# Paladrium - a RPG Project             #
# https://github.com/Kanasaru/Paladrium #
# GPL 3.0 License                       #
#########################################

import pygame
from . import constants
from . import surface

##
# Class: Game ()
# Object holds every information of a running instance of Paladrium
# After inititializing and call start() it runs the gameloop.
##

class Game():
    
    keep_alive = True
    clock = pygame.time.Clock()
    current_sector = surface.Sector1()
    
    def __init__(self, path):
        successes, failures = pygame.init()
        print("{0} successes and {1} failures".format(successes, failures))
        
    def start(self):
        self.screen()
        self.loop()
        
    def screen(self):
        self.screen = pygame.display.set_mode((constants.DISPLAYWIDTH, constants.DISPLAYHEIGHT))
        display_title = "Paladrium - v" + constants.VERSION + " by " + constants.AUTHOR
        pygame.display.set_caption(display_title)
        
    def loop(self):
        while self.keep_alive:
            # eventhandling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.keep_alive = False
     
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
            
            # logic
            
            
            # rendering
            self.screen.fill(constants.BLACK)
            self.current_sector.field_list.draw(self.screen)
            
            pygame.display.flip()
            
            self.clock.tick(constants.FPS)
            
    def exit(self):
        pygame.quit()