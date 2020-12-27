#########################################
# Paladrium - a RPG Project             #
# https://github.com/Kanasaru/Paladrium #
# GPL 3.0 License                       #
#########################################


### IMPORTS & INITIALISATON

# PyGame
import pygame
pygame.init()

# Paladrium modules
from . import settings
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
        # creating needed instances
        self.settings = settings.Settings(path)
        self.eventhandler = events.EventHandler()
        self.clock = pygame.time.Clock()
        
    def start(self):
        # build main window
        self.settings.screen = pygame.display.set_mode(self.settings.get_display_resolution())
        display_title = self.settings.get_game_title() + " - v" + self.settings.get_game_version() + " by " + self.settings.get_game_author()
        pygame.display.set_caption(display_title)
        
        # define first loop parameter
        self.exit_game = False
        self.current_screen = None
        self.new_screen = False
        self.screen_number = self.settings.get_default_screen()
        
        # start the loop
        self.loop()

    def loop(self):
        while not self.exit_game:
            
            # set framerate
            self.clock.tick(self.settings.get_fps())
            
            self.handle_events()
            
            self.run_logic()
            
            self.render()
               
        self.exit()
    
    def handle_events(self):
        # get all raised events
        self.eventhandler.get_events()
        
        # handle current title or sector events
        if self.current_screen is not None:
            self.current_screen.handle_events()
        
        for event in self.eventhandler.events:
            if event.type == pygame.QUIT:
                print('SYSTEM/PyGAME EVENT:', event.type)
                self.exit_game = True
            elif event.type == pygame.USEREVENT:
                print('USEREVENT:', event.e_type)
                if event.e_type == events.QUITGAME:
                    self.exit_game = True
                if event.e_type == events.MAINMENU:
                    self.new_screen = True
                    self.screen_number = 0
                if event.e_type == events.STARTGAME:
                    self.new_screen = True
                    self.screen_number = 1
                    
    def run_logic(self):
        # new screen needed?
        if self.new_screen:
            if self.screen_number == 0:
                self.current_screen = title.Main(self.eventhandler, self.settings)
            elif self.screen_number == 1:
                self.current_screen = title.NewGame(self.eventhandler, self.settings)
            else:
                self.current_screen = title.Error(self.eventhandler, self.settings)
                
            self.new_screen = False
        
        # run logic of current title or sector
        if self.current_screen is not None:
            self.current_screen.run_logic()
        else:
            # build main title screen
            self.current_screen = title.Main(self.eventhandler, self.settings)
    
    def render(self):
        # render current title or sector
        self.current_screen.render()
        
        # showing new frame
        pygame.display.flip()
    
    def exit(self):
        pygame.quit()
     