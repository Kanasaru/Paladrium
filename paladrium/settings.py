#########################################
# Paladrium - a RPG Project             #
# https://github.com/Kanasaru/Paladrium #
# GPL 3.0 License                       #
#########################################

### IMPORTS & INITIALISATON

### CLASSES & FUNCTIONS

##
# Class: Settings()
# Parent: none
# Holds and provides every general information of a running instance of Paladrium
##

class Settings():
    
    ##
    # Method: __init__
    # Class: Settings()
    # @param: (str) path
    # @param: (object EventHandler()) eventhandler
    # @return: none
    # Init all default settings
    ##
    def __init__(self, path, eventhandler):
        ### BASIC INFORMATION
        self.game_title   = "Paladrium"
        self.game_version = "0.1"
        self.game_author  = "Kanasaru"
        self.game_path    = path
        
        self.event_handler = eventhandler
        
        self.exit_game = False
        
        ### SCREEN
        self.fps                    = 60
        self.display_resolution     = (1280, 720)
        self.screen                 = None
        self.current_screen         = None
        self.new_screen             = False
        self.new_screen_number      = 0
        
        ### COLORS
        # basic colors
        self.color_white       = (255, 255, 255)
        self.color_black       = (0, 0, 0)
        
        # game colors
        self.color_background  = (83, 83, 83)
        self.color_border      = (196, 184, 102)
        self.color_text        = (120, 117, 98)
        self.color_highlighted = (250, 244, 205)
        self.color_surfaces    = (122, 115, 64)
        self.color_link        = (247, 232, 129)
        
        ### FONTS
        # standard font
        self.font_std      = 'Comic Sans MS'
        self.font_size_std = 20
        
        ### BUTTONS
        # images
        self.button_image_file       = path + "assets/button.png"
        self.button_hover_image_file = path + "assets/button-clicked.png"
        self.button_down_image_file  = path + "assets/button-clicked.png"
        self.button_text_padding     = (0, 0, 3, 0) # top, right, bottom, left
        
        # size
        self.button_size = (220, 60)

    ##
    # Method: is_exit_game
    # Class: Settings()
    # @param: none
    # @return: (bool)
    # Returns boolean if the game has triggert an exit
    ##
    def is_exit_game(self):
        return self.exit_game
    
    ##
    # Method: set_exit_game
    # Class: Settings()
    # @param: (bool) is_exit
    # @return: (bool)
    # Sets trigger for an exit and returns boolean on success
    ##
    def set_exit_game(self, is_exit):
        if isinstance(is_exit, bool):
            self.exit_game = is_exit
            return True
        
        return False
    
    ##
    # Method: is_new_screen
    # Class: Settings()
    # @param: none
    # @return: (bool)
    # Returns boolean if a new screen has to be loaded
    ##
    def is_new_screen(self):
        return self.new_screen
    
    ##
    # Method: set_new_screen
    # Class: Settings()
    # @param: (bool) is_new_screen
    # @return: (bool)
    # Sets trigger for loading a new screen and returns boolean on success
    ##
    def set_new_screen(self, is_new_screen):
        if isinstance(is_new_screen, bool):
            self.new_screen = is_new_screen
            return True
        
        return False
    
    ##
    # Method: evhandler
    # Class: Settings()
    # @param: none
    # @return: (object)
    # Returns the instance of the event handler
    ##
    def evhandler(self):
        return self.event_handler
    
    ##
    # Method: get_button_text_padding
    # Class: Settings()
    # @param: none
    # @return: (tuple)
    # Returns the text padding for buttons as tuple(top, right, bottom, left)
    ##
    def get_button_text_padding(self):
        return self.button_text_padding
    
    ##
    # Method: get_font_std
    # Class: Settings()
    # @param: none
    # @return: (str)
    # Returns the standard font
    ##
    def get_font_std(self):
        return self.font_std
    
    ##
    # Method: get_font_size_std
    # Class: Settings()
    # @param: none
    # @return: (int)
    # Returns standard font size
    ##
    def get_font_size_std(self):
        return self.font_size_std
    
    ##
    # Method: get_button_image_file
    # Class: Settings()
    # @param: none
    # @return: (str)
    # Returns path for button image
    ##
    def get_button_image_file(self):
        return self.button_image_file
    
    ##
    # Method: get_button_hover_image_file
    # Class: Settings()
    # @param: none
    # @return: (str)
    # Returns path for button hover image
    ##
    def get_button_hover_image_file(self):
        return self.button_hover_image_file

    ##
    # Method: get_button_down_image_file
    # Class: Settings()
    # @param: none
    # @return: (str)
    # Returns path for button down image
    ##
    def get_button_down_image_file(self):
        return self.button_down_image_file
    
    ##
    # Method: get_button_size
    # Class: Settings()
    # @param: (bool) width
    # @param: (bool) height
    # @return: (tulpe) or (int)
    # Returns the button size or only width respectively height by setting other parameter to False
    ##
    def get_button_size(self, width=True, height=True):
        button_width, button_height = self.button_size
        
        if width and not height:
            return button_width
        elif height and not width:
            return button_height
        
        return self.button_size
    
    ##
    # Method: set_button_size
    # Class: Settings()
    # @param: (tulpe) button_size
    # @return: (bool)
    # Sets button size and returns boolean on success
    ##
    def set_button_size(self, button_size):
        if isinstance(button_size, tuple) and len(button_size) == 2:
            button_width, button_height = button_size
            
            if isinstance(button_width, int) and isinstance(button_height, int):
                self.button_size = button_size
                return True
            
        return False
    
    ##
    # Method: get_game_title
    # Class: Settings()
    # @param: none
    # @return: (str)
    # Returns the game title
    ##
    def get_game_title(self):
        return self.game_title
    
    ##
    # Method: get_game_version
    # Class: Settings()
    # @param: none
    # @return: (str)
    # Returns the game version
    ##
    def get_game_version(self):
        return self.game_version
    
    ##
    # Method: get_game_author
    # Class: Settings()
    # @param: none
    # @return: (str)
    # Returns the game author
    ##
    def get_game_author(self):
        return self.game_author

    ##
    # Method: get_fps
    # Class: Settings()
    # @param: none
    # @return: (int)
    # Returns the current framerate
    ##
    def get_fps(self):
        return self.fps
    
    ##
    # Method: set_fps
    # Class: Settings()
    # @param: (int) fps
    # @return: (bool)
    # Sets the framerate and returns boolean on success
    ##
    def set_fps(self, fps):
        if isinstance(fps, int):
            self.fps = fps
            return True
            
        return False
    
    ##
    # Method: get_new_screen_number
    # Class: Settings()
    # @param: none
    # @return: (int)
    # Returns the number of the new screen
    ##
    def get_new_screen_number(self):
        return self.new_screen_number
    
    ##
    # Method: set_new_screen_number
    # Class: Settings()
    # @param: (int) screen_number
    # @return: (bool)
    # Sets the number of the new screen and returns boolean on success
    ##
    def set_new_screen_number(self, screen_number):
        if isinstance(screen_number, int):
            self.new_screen_number = screen_number
            return True
            
        return False
    
    ##
    # Method: get_current_screen
    # Class: Settings()
    # @param: none
    # @return: (object)
    # Returns the current display instance
    ##
    def get_current_screen(self):
        return self.current_screen
    
    ##
    # Method: set_current_screen
    # Class: Settings()
    # @param: (object) screen
    # @return: (bool)
    # Sets the current screen instance
    ##
    def set_current_screen(self, screen):    
        self.current_screen = screen
        return True
    
    ##
    # Method: get_screen
    # Class: Settings()
    # @param: none
    # @return: (object)
    # Returns the main display instance
    ##
    def get_screen(self):
        return self.screen
    
    ##
    # Method: set_screen
    # Class: Settings()
    # @param: (object) screen
    # @return: (bool)
    # Sets the main display instance
    ##
    def set_screen(self, screen):    
        self.screen = screen
        return True
    
    ##
    # Method: get_game_path
    # Class: Settings()
    # @param: none
    # @return: (str)
    # Returns the game path
    ##
    def get_game_path(self):
        return self.game_path
    
    ##
    # Method: color
    # Class: Settings()
    # @param: (str) color_name
    # @return: (tulpe) or (bool)
    # Returns the tulpe of the given color or False by failure
    ##
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
        elif color_name == 'highlight':
            return self.color_highlighted
        elif color_name == 'surface':
            return self.color_surfaces
        elif color_name == 'link':
            return self.color_link
            
        return False
    
    ##
    # Method: get_display_resolution
    # Class: Settings()
    # @param: (bool) width
    # @param: (bool) height
    # @return: (tulpe) or (int)
    # Returns the display resolution or only width respectively height by setting other parameter to False
    ##
    def get_display_resolution(self, width=True, height=True):
        display_width, display_height = self.display_resolution
        
        if width and not height:
            return display_width
        elif height and not width:
            return display_height
        
        return self.display_resolution
    
    ##
    # Method: set_display_resolution
    # Class: Settings()
    # @param: (tulpe) resolution
    # @return: (bool)
    # Sets display resolution and returns boolean on success
    ##
    def set_display_resolution(self, resolution):
        if isinstance(resolution, tuple) and len(resolution) == 2:
            display_width, display_height = resolution
            
            if isinstance(display_width, int) and isinstance(display_height, int):
                self.display_resolution = resolution
                return True
            
        return False
