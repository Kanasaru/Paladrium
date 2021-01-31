"""This module contains settings functionality

:class Settings: contains general settings

.. note:: https://github.com/Kanasaru/Paladrium
.. note:: exports settings object
.. note:: raises no exceptions

"""
import mpos.msg
import mpos.helpers.debug as debug
import mpos.forms
from paladrium.logger import log

MODUL = __name__

class Settings():
    """This class provides and manages the general settings.
    
    :method __init__: sets up the basic settings
    :method is_resolution: checks if resolution matches settings
    :method set_current_title: sets current title
    :method get_current_title: returns current title
    :method get_font_std: returns standard font
    :method get_font_size_std: returns standard font size
    :method get_game_title: returns game title
    :method get_game_version: returns game version
    :method get_game_author: returns game author
    :method get_fps: returns frames per second value
    :method set_fps: sets frames per second
    :method color: retruns color by its name
    :method get_display_resolution: returns display resolution
    :method set_display_resolution: sets display resolution
    
    """
    def __init__(self):
        """Sets up the basic settings.
        
        :Example:
        
        >>> from paladrium.settings import settings
        
        """
        self.NAME = self.__class__.__name__
        
        self.game_title = "Paladrium"
        self.game_version = "0.2 (alpha)"
        self.game_author = "Kanasaru"
        
        self.fps = 60
        self.display_resolution = (1280, 720)
        
        self.color_white = (255, 255, 255)
        self.color_black = (0, 0, 0)
        
        self.color_background = (83, 83, 83)
        self.color_border = (196, 184, 102)
        self.color_text = (0, 0, 0)
        self.color_text_hover = (120, 117, 98)
        self.color_highlighted = (250, 244, 205)
        self.color_surfaces = (122, 115, 64)
        self.color_link = (247, 232, 129)
        
        self.font_std = "assets/fonts/Cinzel-Medium.ttf"
        self.font_size_std = 20
        
        self.current_title = None
        
        self.set_display_resolution(self.display_resolution)
        
    def is_resolution(self, resolution):
        """Checks if resolution matches settings.
        
        :param resolution: reolution that needs to be checked
        :type resolution: tuple
        :returns: True if resolution matches
        :rtype: bool
        
        """
        if resolution == self.display_resolution:
            return True
        else:
            return False
            
    def set_current_title(self, title):
        """Sets current title.
        
        :param title: title to be set as current
        :type title: mpos.forms.title.Title
        :returns: True on success
        :rtype: bool
        
        """
        if isinstance(title, mpos.forms.title.Title):
            self.current_title = title
        else:
            log.info(mpos.msg.echo(MODUL, self.NAME, "Wrong type"))
            return False
        
        return True
        
    def get_current_title(self):
        """Returns current title.
        
        :returns: current title
        :rtype: mpos.forms.title.Title
        
        """
        if self.current_title is not None:
            return self.current_title
        
        return False
        
    def get_font_std(self):
        """Returns standard font.
        
        :returns: standard font
        :rtype: str
        
        """
        return self.font_std
        
    def get_font_size_std(self):
        """Returns standard font size.
        
        :returns: standard font size
        :rtype: int
        
        """
        return self.font_size_std
        
    def get_game_title(self):
        """Returns game title.
        
        :returns: game title
        :rtype: str
        
        """
        return self.game_title
        
    def get_game_version(self):
        """Returns game version.
        
        :returns: game version
        :rtype: str
        
        """
        return self.game_version
        
    def get_game_author(self):
        """Returns game author.
        
        :returns: game author
        :rtype: str
        
        """
        return self.game_author
        
    def get_fps(self):
        """Returns frames per second value.
        
        :returns: current frames per second
        :rtype: int
        
        """
        return self.fps
        
    def set_fps(self, fps):
        """Sets frames per second.
        
        :param fps: frames per second
        :type fps: int
        :returns: True on success
        :rtype: bool
        
        """
        if isinstance(fps, int):
            self.fps = fps
            return True
        else:
            log.info(mpos.msg.echo(MODUL, self.NAME, "Wrong type"))
            return False
            
    def color(self, color_name):
        """Retruns color by its name.
        
        :param color_name: name of color
        :type color_name: str
        :returns: colors tuple
        :rtype: tuple
        
        """
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
        """Returns display resolution.
        
        :param width: True if width is needed
        :param height: True if height is needed
        :type width: bool
        :type height: bool
        :returns: resolution or width or height
        :rtype: tuple or int
        
        """
        display_width, display_height = self.display_resolution
        
        if width and not height:
            return display_width
        elif height and not width:
            return display_height
        else:
            return self.display_resolution
            
    def set_display_resolution(self, resolution):
        """Sets display resolution.
        
        :param resolution: resolution to be set
        :type resolution: tuple
        :returns: True on success
        :rtype: bool
        
        """
        if isinstance(resolution, tuple) and len(resolution) == 2:
            display_width, display_height = resolution
            
            if isinstance(display_width, int):
                if isinstance(display_height, int):
                    self.display_resolution = resolution
                    return True
            else:
                log.info(mpos.msg.echo(MODUL, self.NAME, "Wrong type"))
        else:
            log.info(mpos.msg.echo(MODUL, self.NAME, "Wrong type"))
                
        return False
        
settings = Settings()
