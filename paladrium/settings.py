#########################################
# Paladrium - a RPG Project             #
# https://github.com/Kanasaru/Paladrium #
# GPL 3.0 License                       #
#########################################


class Settings():
    
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

    def is_exit_game(self):
        return self.exit_game
        
    def set_exit_game(self, is_exit):
        if isinstance(is_exit, bool):
            self.exit_game = is_exit
            return True
        
        return False
    
    def is_new_screen(self):
        return self.new_screen
        
    def set_new_screen(self, is_new_screen):
        if isinstance(is_new_screen, bool):
            self.new_screen = is_new_screen
            return True
        
        return False
        
    def evhandler(self):
        return self.event_handler
        
    def get_button_text_padding(self):
        return self.button_text_padding
    
    def get_screen(self):
        return self.screen
    
    def get_font_std(self):
        return self.font_std
        
    def get_font_size_std(self):
        return self.font_size_std
        
    def get_button_image_file(self):
        return self.button_image_file
    
    def get_button_hover_image_file(self):
        return self.button_hover_image_file

    def get_button_down_image_file(self):
        return self.button_down_image_file
        
    def get_button_size(self, width=True, height=True):
        button_width, button_height = self.button_size
        
        if width and not height:
            return button_width
        elif height and not width:
            return button_height
        
        return self.button_size
    
    def set_button_size(self, button_size):
        if isinstance(button_size, tuple) and len(button_size) == 2:
            button_width, button_height = button_size
            
            if isinstance(button_width, int) and isinstance(button_height, int):
                self.button_size = button_size
                return True
            
        return False
        
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
            
        return False
    
    def get_new_screen_number(self):
        return self.new_screen_number
        
    def set_new_screen_number(self, screen_number):
        if isinstance(screen_number, int):
            self.new_screen_number = screen_number
            return True
            
        return False
        
    def get_current_screen(self):
        return self.current_screen
        
    def set_current_screen(self, screen):    
        self.current_screen = screen
        return True
        
    def get_game_path(self):
        return self.game_path
        
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
        
    def get_display_resolution(self, width=True, height=True):
        display_width, display_height = self.display_resolution
        
        if width and not height:
            return display_width
        elif height and not width:
            return display_height
        
        return self.display_resolution
    
    def set_display_resolution(self, resolution):
        if isinstance(resolution, tuple) and len(resolution) == 2:
            display_width, display_height = resolution
            
            if isinstance(display_width, int) and isinstance(display_height, int):
                self.display_resolution = resolution
                return True
            
        return False
