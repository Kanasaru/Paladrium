#########################################
# Paladrium - a RPG Project             #
# https://github.com/Kanasaru/Paladrium #
# GPL 3.0 License                       #
#########################################


### IMPORTS & INITIALISATON

# PyGame
import pygame
pygame.init()

# MPoS
import mpos

# Paladrium
from paladrium.logger import log
from paladrium.settings import settings
import paladrium.titles

### CONSTANTS


### CLASSES & FUNCTIONS

class Game():
    
    def __init__(self):
        
        # variables for event handling, logic and rendering
        self.game_running      = False
        self.exit_game         = False
        self.new_title         = None
        self.resolution_update = None
        
        attr = {
            "pos_x":            0,
            "pos_y":            settings.get_display_resolution(False, True) - 100,
            "width":            settings.get_display_resolution(True, False),
            "height":           100
        }
        self.debug    = mpos.helpers.debug.DebugScreen(attr)
        
        self.clock    = pygame.time.Clock()
        
        # build main window
        self.surface = pygame.display.set_mode(settings.get_display_resolution())
        display_title = settings.get_game_title() + " - v" + settings.get_game_version() + " by " + settings.get_game_author()
        pygame.display.set_caption(display_title)
        
        # set current title
        settings.set_current_title(paladrium.titles.build_title(paladrium.titles.MAIN))
        
        # start the loop
        self.loop()
        
    def loop(self):
        
        # while no exit event is raised
        while not self.exit_game:
            
            # set framerate
            self.clock.tick(settings.get_fps())
            
            # handle game events
            self.handle_events()
            
            # run game logic
            self.run_logic()
            
            # show everything
            self.render()
        
        # clean ending after exit event
        self.exit()
        
    def handle_events(self):
        
        # if game is not running handle current title events
        if not self.game_running:
            # look up for events in current title
            for event in settings.get_current_title().get_events():
                # load new title?
                if event.code == paladrium.events.NEWTITLE:
                    self.new_title = event.data
                # change display resolution?
                elif event.code == paladrium.events.RESOLUTION:
                    self.resolution_update = event.data
                # start a game?
                elif event.code == paladrium.events.STARTGAME:
                    self.game_running = True
                # quit Paladrium?
                elif event.code == paladrium.events.QUITGAME:
                    self.exit_game = True
                    
                # print every event for debugging
                log.info(event)
                
            # clear title event queue
            settings.get_current_title().clear_events()
            
            # look up for pygame events
            for event in pygame.event.get():
                # handle event by current title
                settings.get_current_title().handle_event(event)
                
                # quit Paladrium?
                if event.type == pygame.QUIT:
                    self.exit_game = True
                
                # toggle debug?
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_F3:
                        self.debug.toggle()
                    
        # game is running
        else:
            for event in pygame.event.get():
                # quit Paladrium?
                if event.type == pygame.QUIT:
                    self.exit_game = True
                    log.info("PyGame QUIT")
            
    def run_logic(self):
        
        # if game is not running run current title logic
        if not self.game_running:
            # resolutin changed?
            if self.resolution_update is not None:
                # change display mode and update settings
                settings.set_display_resolution(self.resolution_update)
                pygame.display.set_mode(self.settings.get_display_resolution())
                # rebuild title
                settings.set_current_title(paladrium.titles.build_title(paladrium.titles.RESOLUTION))
                # all done so prevent updating it again
                self.resolution_update = None
            
            # new title needed?
            if self.new_title is not None:
                # change current title to new title
                settings.set_current_title(paladrium.titles.build_title(self.new_title))
                # all done so prevent changing it again
                self.new_title = None
                
            # run logic of current title
            settings.get_current_title().run_logic()
        
        attr = {
            "pos_y":            settings.get_display_resolution(False, True) - 100,
            "width":            settings.get_display_resolution(True, False),
        }
        self.debug.set_attr(attr)
        self.debug.run_logic()
            
    def render(self):
        
        # if game is not running render current title
        if not self.game_running:
            settings.get_current_title().render(self.surface)
        
        self.debug.render(self.surface)
            
        # show what we got
        pygame.display.flip()
        
    def exit(self):
        
        # exit pygame instance
        pygame.quit()
