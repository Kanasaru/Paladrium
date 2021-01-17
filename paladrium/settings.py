#########################################
# Paladrium - a RPG Project             #
# https://github.com/Kanasaru/Paladrium #
# GPL 3.0 License                       #
#########################################

### IMPORTS & INITIALISATON

import mpos.helpers.debug as debug
import mpos.forms

from paladrium.logger import log

### CONSTANTS

### CLASSES & FUNCTIONS

class Settings():
    
    def __init__(self):
        
        ### BASIC INFORMATION
        self.game_title   = "Paladrium"
        self.game_version = "0.1"
        self.game_author  = "Kanasaru"
        
        ### SCREEN
        self.fps                    = 60
        self.display_resolution     = (1280, 720)
        
        ### COLORS
        # basic colors
        self.color_white       = (255, 255, 255)
        self.color_black       = (0, 0, 0)
        
        # game colors
        self.color_background  = (83, 83, 83)
        self.color_border      = (196, 184, 102)
        self.color_text        = (0, 0, 0)
        self.color_text_hover  = (120, 117, 98)
        self.color_highlighted = (250, 244, 205)
        self.color_surfaces    = (122, 115, 64)
        self.color_link        = (247, 232, 129)
        
        ### FONTS
        # standard font
        self.font_std      = "assets/fonts/Cinzel-Medium.ttf"
        self.font_size_std = 20
        
        ### MENU
        self.current_title = None
        
        self.set_display_resolution(self.display_resolution)
        
    def is_resolution(self, resolution):
        if resolution == self.display_resolution:
            return True
        else:
            return False
            
    def set_current_title(self, title):
        if isinstance(title, mpos.forms.title.Title):
            self.current_title = title
        else:
            log.info("Settings().set_current_title(): Only type (forms.Title) allowed")
            return False
        
        return True
        
    def get_current_title(self):
        if self.current_title is not None:
            return self.current_title
        
        return False
        
    def get_font_std(self):
        return self.font_std
        
    def get_font_size_std(self):
        return self.font_size_std
        
    def get_game_title(self):
        return self.game_title
        
    def get_game_version(self):
        return self.game_version
        
    def get_game_author(self):
        return self.game_author
        
    def get_fps(self):
        return self.fps
        
    def set_fps(self, fps):
        if isinstance(fps, int):
            self.fps = fps
            return True
        else:
            log.info("Settings().set_fps(): Only type (int) allowed")
            return False
            
    def color(self, color_name):
        if color_name == 'white':
            return self.color_white
        elif color_name == 'black':
            return self.color_black
        elif color_name == 'background':
            return self.color_background
        elif color_name == 'border':
            return self.color_border
        elif color_name == 'text':
            return self.color_text
        elif color_name == 'text hover':
            return self.color_text_hover
        elif color_name == 'highlight':
            return self.color_highlighted
        elif color_name == 'surface':
            return self.color_surfaces
        elif color_name == 'link':
            return self.color_link
            
        return False
        
    def get_display_resolution(self, width=True, height=True):
        
        # get current resolution
        display_width, display_height = self.display_resolution
        
        # asking only for width?
        if width and not height:
            return display_width
            
        # asking only for height?
        elif height and not width:
            return display_height
        
        # give everything
        else:
            return self.display_resolution
            
    def set_display_resolution(self, resolution):
        global DEBUGMODE
        
        # check if given resolution is ok
        if isinstance(resolution, tuple) and len(resolution) == 2:
            display_width, display_height = resolution
            
            if isinstance(display_width, int) and isinstance(display_height, int):
                # apply given resolution
                self.display_resolution = resolution
                return True
            else:
                log.info("Settings().set_display_resolution(): Only type (int) in given resolution allowed")
        else:
            log.info("Settings().set_display_resolution(): Given resolution has to be a (tuple) with len = 2")
                
        return False
        
settings = Settings()
