"""This module contains constants, functions and classes for
sprite handling

:class SpriteSheet: handles sprite sheets

.. note:: exports no objects
.. note:: raises no exceptions
.. todo:: find a way to handle init error

"""
import pygame
import mpos.msg
from mpos.helpers.logger import log

MODUL = __name__

class SpriteSheet():
    """This class handles sprite sheets.
    
    :method __init__: loads the sprite sheet
    :method image_at: loads a single sprite from sheet
    :method images_at: loads a multiple sprites from sheet
    
    .. note:: code is taken and slightly edited from
        www.scriptefun.com/transcript-2-using
        sprite-sheets-and-drawing-the-background
    
    """
    def __init__(self, filename, sprite_size):
        """Loads the sprite sheet.
        
        :param filename: contains filepath of the sheet
        :type filename: filepath or str
        
        :Example:
        
        >>> import pygame
        >>> import mpos.helpers
        >>> pygame.init()
        >>> a = mpos.helpers.spritesheet.SpriteSheet("file.png")
        
        """
        self.NAME = self.__class__.__name__
        
        try:
            self.sheet = pygame.image.load(filename).convert()
            self.sheet_size = self.sheet.get_size()
            self.sprite_size = sprite_size
        except:
            log.error(mpos.msg.echo(
                MODUL,
                self.NAME,
                mpos.msg.E_FILE,
                str(filename)
            ))
            
    def image_at(self, rectangle, colorkey=None):
        """Loads a single sprite from sheet.
        
        :param rectangle: position and size of sprite in sheet
        :param colorkey: sets surface colokey if given
        :type rectangle: pygame.Rect or tuple (len 4)
        :type colorkey: tuple (len 3)
        :returns: single sprite as surface
        :rtype: pygame.Surface
        
        :Example:
        
        >>> import pygame
        >>> import mpos.helpers
        >>> pygame.init()
        >>> a = mpos.helpers.spritesheet.SpriteSheet("file.png")
        >>> img_surface = a.image_at((0, 0, 16, 16))
        
        """
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
            
        return image
        
    def image_rotate(self, image, angle):
        
        image_new = pygame.transform.rotate(image, angle)
        return image_new
    
    def images_at(self, rects, colorkey=None):
        """Loads a multiple sprites from sheet.
        
        :param rects: position and sizes of sprites in sheet
        :param colorkey: sets surface colokey if given
        :type rects: list of pygame.Rect or tuple (len 4)
        :type colorkey: tuple (len 3)
        :returns: list of sprites as surfaces
        :rtype: list
        
        :Example:
        
        >>> import pygame
        >>> import mpos.helpers
        >>> pygame.init()
        >>> a = mpos.helpers.spritesheet.SpriteSheet("file.png")
        >>> img_surfaces = a.images_at((0, 0, 16, 16), (17, 0, 16, 16))
        
        """
        return [self.image_at(rect, colorkey) for rect in rects]
