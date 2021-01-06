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
from . import forms
from . import events
from . import titles

### CONSTANTS


### CLASSES & FUNCTIONS

##
# Class: Game()
# Parent: none
##
class Game():

    ##
    # Method: __init__
    # Class: Game()
    # @param: none
    # @return: none
    ##
    def __init__(self):
        
        # variables for event handling, logic and rendering
        self.game_running      = False
        self.exit_game         = False
        self.new_title         = None
        self.resolution_update = None
        
        # creating needed instances
        self.settings = settings.Settings()
        self.clock = pygame.time.Clock()
        
        # build main window
        pygame.display.set_mode(self.settings.get_display_resolution())
        display_title = self.settings.get_game_title() + " - v" + self.settings.get_game_version() + " by " + self.settings.get_game_author()
        pygame.display.set_caption(display_title)
        
        # set current title
        self.settings.set_current_title(self.build_title(titles.MAIN))
        
        # start the loop
        self.loop()

    ##
    # Method: loop
    # Class: Game()
    # @param: none
    # @return: none
    ##
    def loop(self):
        
        # while no exit event is raised
        while not self.exit_game:
            
            # set framerate
            self.clock.tick(self.settings.get_fps())
            
            # handle game events
            self.handle_events()
            
            # run game logic
            self.run_logic()
            
            # show everything
            self.render()
        
        # clean ending after exit event
        self.exit()
        
    ##
    # Method: handle_events
    # Class: Game()
    # @param: none
    # @return: none
    ##
    def handle_events(self):
        
        # if game is not running handle current title events
        if not self.game_running:
            # look up for events in current title
            for event in self.settings.get_current_title().get_events():
                # load new title?
                if event.code == events.NEWTITLE:
                    self.new_title = event.data
                # change display resolution?
                elif event.code == events.RESOLUTION:
                    self.resolution_update = event.data
                # start a game?
                elif event.code == events.STARTGAME:
                    self.game_running = True
                # quit Paladrium?
                elif event.code == events.QUITGAME:
                    self.exit_game = True
                    
                # print every event for debugging
                print(event)
                
            # clear title event queue
            self.settings.get_current_title().clear_events()
            
            # look up for pygame events
            for event in pygame.event.get():
                # handle event by current title
                self.settings.get_current_title().handle_event(event)
                
                # quit Paladrium?
                if event.type == pygame.QUIT:
                    self.exit_game = True
                    
        # game is running
        else:
            for event in pygame.event.get():
                # quit Paladrium?
                if event.type == pygame.QUIT:
                    self.exit_game = True
            
    ##
    # Method: run_logic
    # Class: Game()
    # @param: none
    # @return: none
    ##
    def run_logic(self):
        
        # if game is not running run current title logic
        if not self.game_running:
            # resolutin changed?
            if self.resolution_update is not None:
                # change display mode and update settings
                pygame.display.set_mode(self.resolution_update)
                self.settings.set_display_resolution(self.resolution_update)
                # rebuild title
                self.settings.set_current_title(self.build_title(titles.RESOLUTION))
                # all done so prevent updating it again
                self.resolution_update = None
            
            # new title needed?
            if self.new_title is not None:
                # change current title to new title
                self.settings.set_current_title(self.build_title(self.new_title))
                # all done so prevent changing it again
                self.new_title = None
                
            # run logic of current title
            self.settings.get_current_title().run_logic()
            
    ##
    # Method: render
    # Class: Game()
    # @param: none
    # @return: none
    ##
    def render(self):
        
        # if game is not running render current title
        if not self.game_running:
            self.settings.get_current_title().render()
        
        # show what we got
        pygame.display.flip()
        
    ##
    # Method: exit
    # Class: Game()
    # @param: none
    # @return: none
    ##
    def exit(self):
        
        # exit pygame instance
        pygame.quit()
        
    ##
    # Method: build_title
    # Class: Game()
    # @param: (int) identifier
    # @return: (forms.Title) title
    ##
    def build_title(self, identifier):
        
        # create a title
        title = forms.Title(self.settings.color('background'))
        
        # build up Paladrium headline
        attr = {
            "pos-x":        self.settings.get_display_resolution(True, False) / 2,
            "pos-y":        20,
            "text":         "Paladrium",
            "text-size":    60,
        }
        tf_headline = forms.Textfield(attr)
        
        # add headline to title
        title.add(tf_headline)
        
        # stay away, next forms object
        width, height = tf_headline.get_dimensions()
        position_y = height + 100
        
        # which title has to be build?
        if identifier == titles.MAIN:
            
            # build up button
            attr = {
                "pos-y":            position_y,
                "text":             "New Game",
                "callback_event":   events.Event(events.NEWTITLE, titles.NEWGAME)
            }
            b_newgame = forms.Button(attr)
            
            # apply padding
            pos_x = self.settings.get_display_resolution(True, False) / 2 - b_newgame.get_attr("width") / 2
            b_newgame.set_attr(("pos-x", pos_x))
            
            # stay away, next forms object
            width, height = b_newgame.get_dimensions()
            position_y += height + 20
            
            # build up button
            attr = {
                "pos-y":          position_y,
                "text":           "Load Game",
                "callback_event": events.Event(events.LOADGAME, ""),
                "clickable":      False
            }
            b_loadgame = forms.Button(attr)
            
            # apply padding
            pos_x = self.settings.get_display_resolution(True, False) / 2 - b_loadgame.get_attr("width") / 2
            b_loadgame.set_attr(("pos-x", pos_x))
            
            # stay away, next forms object
            width, height = b_loadgame.get_dimensions()
            position_y += height + 20
            
            # build up button
            attr = {
                "pos-y":          position_y,
                "text":           "Options",
                "callback_event": events.Event(events.NEWTITLE, titles.OPTIONS)
            }
            b_options = forms.Button(attr)
            
            # apply padding
            pos_x = self.settings.get_display_resolution(True, False) / 2 - b_options.get_attr("width") / 2
            b_options.set_attr(("pos-x", pos_x))
            
            # stay away, next forms object
            width, height = b_options.get_dimensions()
            position_y += height + 20
            
            # build up button
            attr = {
                "pos-y":          position_y,
                "text":           "Quit Game",
                "callback_event": events.Event(events.QUITGAME, "")
            }
            b_quitgame = forms.Button(attr)
            
            # apply padding
            pos_x = self.settings.get_display_resolution(True, False) / 2 - b_quitgame.get_attr("width") / 2
            b_quitgame.set_attr(("pos-x", pos_x))
            
            # add forms objects to title
            title.add(b_newgame)
            title.add(b_loadgame)
            title.add(b_options)
            title.add(b_quitgame)
            
        elif identifier == titles.NEWGAME:
            
            # build up button
            attr = {
                "pos-y":            position_y,
                "text":             "Start Game",
                "callback_event":   events.Event(events.STARTGAME, "")
            }
            b_startgame = forms.Button(attr)
            
            # apply padding
            pos_x = self.settings.get_display_resolution(True, False) / 2 - b_startgame.get_attr("width") / 2
            b_startgame.set_attr(("pos-x", pos_x))
            
            # stay away, next forms object
            width, height = b_startgame.get_dimensions()
            position_y += height + 20
            
            # build up button
            attr = {
                "pos-y":          position_y,
                "text":           "Back",
                "callback_event": events.Event(events.NEWTITLE, titles.MAIN)
            }
            b_back = forms.Button(attr)
            
            # apply padding
            pos_x = self.settings.get_display_resolution(True, False) / 2 - b_back.get_attr("width") / 2
            b_back.set_attr(("pos-x", pos_x))
            
            # add forms objects to title
            title.add(b_startgame)
            title.add(b_back)
            
        elif identifier == titles.OPTIONS:
            
            # build up button
            attr = {
                "pos-y":            position_y,
                "text":             "Resolutions",
                "callback_event":   events.Event(events.NEWTITLE, titles.RESOLUTION)
            }
            b_resolution = forms.Button(attr)
            
            # apply padding
            pos_x = self.settings.get_display_resolution(True, False) / 2 - b_resolution.get_attr("width") / 2
            b_resolution.set_attr(("pos-x", pos_x))
            
            # stay away, next forms object
            width, height = b_resolution.get_dimensions()
            position_y += height + 20
            
            # build up button
            attr = {
                "pos-y":          position_y,
                "text":           "Sounds",
                "callback_event": events.Event(events.NEWTITLE, titles.SOUNDS),
                "clickable":      False
            }
            b_sounds = forms.Button(attr)
            
            # apply padding
            pos_x = self.settings.get_display_resolution(True, False) / 2 - b_sounds.get_attr("width") / 2
            b_sounds.set_attr(("pos-x", pos_x))
            
            # stay away, next forms object
            width, height = b_sounds.get_dimensions()
            position_y += height + 20
            
            # build up button
            attr = {
                "pos-y":          position_y,
                "text":           "Controls",
                "callback_event": events.Event(events.NEWTITLE, titles.CONTROLS),
                "clickable":      False
            }
            b_controls = forms.Button(attr)
            
            # apply padding
            pos_x = self.settings.get_display_resolution(True, False) / 2 - b_controls.get_attr("width") / 2
            b_controls.set_attr(("pos-x", pos_x))
            
            # stay away, next forms object
            width, height = b_controls.get_dimensions()
            position_y += height + 20
            
            # build up button
            attr = {
                "pos-y":          position_y,
                "text":           "Back",
                "callback_event": events.Event(events.NEWTITLE, titles.MAIN)
            }
            b_back = forms.Button(attr)
            
            # apply padding
            pos_x = self.settings.get_display_resolution(True, False) / 2 - b_back.get_attr("width") / 2
            b_back.set_attr(("pos-x", pos_x))
            
            # add forms objects to title
            title.add(b_resolution)
            title.add(b_sounds)
            title.add(b_controls)
            title.add(b_back)
            
        elif identifier == titles.RESOLUTION:
            
            # build up button
            if self.settings.is_resolution((640, 480)):
                clickable = False
            else:
                clickable = True
            
            attr = {
                "pos-y":            position_y,
                "text":             "640 x 480",
                "callback_event":   events.Event(events.RESOLUTION, (640, 480)),
                "clickable":        clickable
            }
            b_resolution_640 = forms.Button(attr)
            
            # apply padding
            pos_x = self.settings.get_display_resolution(True, False) / 2 - b_resolution_640.get_attr("width") / 2
            b_resolution_640.set_attr(("pos-x", pos_x))
            
            # stay away, next forms object
            width, height = b_resolution_640.get_dimensions()
            position_y += height + 20
            
            # build up button
            if self.settings.is_resolution((1280, 720)):
                clickable = False
            else:
                clickable = True
            
            attr = {
                "pos-y":            position_y,
                "text":             "1280 x 720",
                "callback_event":   events.Event(events.RESOLUTION, (1280, 720)),
                "clickable":        clickable
            }
            b_resolution_1280 = forms.Button(attr)
            
            # apply padding
            pos_x = self.settings.get_display_resolution(True, False) / 2 - b_resolution_1280.get_attr("width") / 2
            b_resolution_1280.set_attr(("pos-x", pos_x))
            
            # stay away, next forms object
            width, height = b_resolution_1280.get_dimensions()
            position_y += height + 20
            
            # build up button
            attr = {
                "pos-y":          position_y,
                "text":           "Back",
                "callback_event": events.Event(events.NEWTITLE, titles.OPTIONS)
            }
            b_back = forms.Button(attr)
            
            # apply padding
            pos_x = self.settings.get_display_resolution(True, False) / 2 - b_back.get_attr("width") / 2
            b_back.set_attr(("pos-x", pos_x))
            
            # add forms objects to title
            title.add(b_resolution_640)
            title.add(b_resolution_1280)
            title.add(b_back)
            
        else:
            # for debugging if given title does not exist
            print("Game().build_title(): Given title does not exist")
            
        return title
     