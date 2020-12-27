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
# Parent: none
# After inititializing and it runs the gameloop
##

class Game():

    ##
    # Method: __init__
    # Class: Game()
    # @param: (str) path
    # @return: none
    # Init main instances, builds up main window and starts loop
    ##
    def __init__(self, path):
        # creating needed instances
        self.settings = settings.Settings(path, events.EventHandler())
        self.clock = pygame.time.Clock()
        
        # build main window
        self.settings.set_screen(pygame.display.set_mode(self.settings.get_display_resolution()))
        display_title = self.settings.get_game_title() + " - v" + self.settings.get_game_version() + " by " + self.settings.get_game_author()
        pygame.display.set_caption(display_title)
        
        # start the loop
        self.loop()

    ##
    # Method: loop
    # Class: Game()
    # @param: none
    # @return: none
    # Starts game loop, sets framerate and calls event/logic/render-handler
    ##
    def loop(self):
        while not self.settings.is_exit_game():
            
            # set framerate
            self.clock.tick(self.settings.get_fps())
            
            self.handle_events()
            
            self.run_logic()
            
            self.render()
               
        self.exit()
    
    ##
    # Method: handle_events
    # Class: Game()
    # @param: none
    # @return: none
    # Does all event handling and calls every event handling function/method
    ##
    def handle_events(self):
        # collect all raised events
        self.settings.evhandler().collect_events()
        
        # handle current title or sector events
        if self.settings.get_current_screen() is not None:
            self.settings.get_current_screen().handle_events()
        
        for event in self.settings.evhandler().get_events():
            if event.type == pygame.QUIT:
                print('SYSTEM/PyGAME EVENT:', event.type)
                self.settings.set_exit_game(True)
            elif event.type == pygame.USEREVENT:
                print('USEREVENT:', event.e_type)
                if event.e_type == self.settings.evhandler().QUITGAME:
                    self.settings.set_exit_game(True)
                if event.e_type == self.settings.evhandler().MAINMENU:
                    self.settings.set_new_screen(True)
                    self.settings.set_new_screen_number(0)
                if event.e_type == self.settings.evhandler().STARTGAME:
                    self.settings.set_new_screen(True)
                    self.settings.set_new_screen_number(1)
    
    ##
    # Method: run_logic
    # Class: Game()
    # @param: none
    # @return: none
    # Does all logic based on events and settings
    ##            
    def run_logic(self):
        # new screen needed?
        if self.settings.is_new_screen():
            if self.settings.get_new_screen_number() == 0:
                self.settings.set_current_screen(title.Main(self.settings))
            elif self.settings.get_new_screen_number() == 1:
                self.settings.set_current_screen(title.NewGame(self.settings))
            else:
                self.settings.set_current_screen(title.Error(self.settings))
                
            self.settings.set_new_screen(False)
        
        # run logic of current title or sector
        if self.settings.get_current_screen() is not None:
            self.settings.get_current_screen().run_logic()
        else:
            # build main title screen
            self.settings.set_current_screen(title.Main(self.settings))
    
    ##
    # Method: render
    # Class: Game()
    # @param: none
    # @return: none
    # Draws on main surface and calls every rendering function/method
    ##
    def render(self):
        # render current title or sector
        self.settings.get_current_screen().render()
        
        # showing new frame
        pygame.display.flip()
    
    ##
    # Method: exit
    # Class: Game()
    # @param: none
    # @return: none
    # Exit procedure for clean shutdown 
    ##
    def exit(self):
        pygame.quit()
     