"""This module contains constants, functions and classes for
mpos.forms.button handling

:class Button: creates a button

.. note:: exports no objects
.. note:: raises no exceptions
.. todo:: get rid of general paths

"""
import pygame
import mpos.msg
import mpos.helpers.attr
import mpos.helpers.spritesheet
from mpos.helpers.logger import log

MODUL = __name__

class Button(pygame.sprite.Sprite):
    """This class provides and manages the general button of
    mpos.forms.button that can be added to a title.
    
    :method __init__: sets up the basic button
    :method set_attr: sets one or multiple button attributes
    :method get_attr: returns button attribute(s)
    :method update: updates button by own attributes values
    :method get_events: returns all events
    :method clear_events: clears the event list
    :method handle_event: handles an event
    :method get_dimensions: returns button size
    :method width: returns button width
    :method height: returns button height
    
    .. note: initial source code by skrx from stackoverflow.com
        (https://stackoverflow.com/users/6220679/skrx)
    
    """
    def __init__(self, attributes=None):
        """Sets up the basic button.
        
        :param attributes: contains settings of the button
        :type attributes: dict
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> b = mpos.forms.button.Button()
        >>> args = {"width": 100, "height": 20}
        >>> a = mpos.forms.button.Button(args)
        
        """
        self.NAME = self.__class__.__name__
        
        pygame.sprite.Sprite.__init__(self)
        
        self.events = []
        self.attr = {
            "pos_x": 0,
            "pos_y": 0,
            "width": 220,
            "height": 60,
            "text": "",
            "callback_event": None,
            "clickable": True,
            "spritesheet": None,
            "text_font": "assets/fonts/Cinzel-Medium.ttf",
            "font_size": 20,
            "font_color": (0, 0 ,0),
            "font_color_hover": (120, 117, 98),
            "font_color_down": (120, 117, 98),
            "font_color_disabled": (0, 0 ,0),
            "bg_color": (255, 255, 255),
            "colorkey": (0, 0, 0),
        }
        if attributes is not None:
            self.set_attr(attributes)
        
        self.font = pygame.font.Font(
            self.attr["text_font"],
            self.attr["font_size"]
        )
        
        self.surf_images = {
            "image_normal": None,
            "image_hover": None,
            "image_down": None,
            "image_disabled": None
        }
        
        for key in self.surf_images:
            self.surf_images[key] = pygame.Surface((
                self.attr["width"],
                self.attr["height"]
            ))
            self.surf_images[key].fill(self.attr["bg_color"])
            self.surf_images[key].set_colorkey(self.attr["colorkey"])
        
        if self.attr["spritesheet"] is not None:
            self.spritesheet = mpos.helpers.spritesheet.SpriteSheet(
                self.attr["spritesheet"],
                (self.attr["width"], self.attr["height"])
            )
            
            self.surf_images["image_normal"] = self.spritesheet.image_at(
                (
                    0,
                    0,
                    self.attr["width"],
                    self.attr["height"]
                ),
                self.attr["colorkey"]
            )
            self.surf_images["image_hover"] = self.spritesheet.image_at(
                (
                    0,
                    self.attr["height"],
                    self.attr["width"],
                    self.attr["height"]
                ),
                self.attr["colorkey"]
            )
            self.surf_images["image_down"] = self.spritesheet.image_at(
                (
                    0,
                    self.attr["height"]*2,
                    self.attr["width"],
                    self.attr["height"]
                ),
                self.attr["colorkey"]
            )
            self.surf_images["image_disabled"] = self.spritesheet.image_at(
                (
                    0,
                    self.attr["height"]*3,
                    self.attr["width"],
                    self.attr["height"]
                ),
                self.attr["colorkey"]
            )
        
        if self.attr["clickable"]:
            self.image = self.surf_images["image_normal"]
        else:
            self.image = self.surf_images["image_disabled"]
        
        self.rect = self.image.get_rect(topleft=(
            self.attr["pos_y"],
            self.attr["pos_x"]
        ))
        
        image_center_x, image_center_y = self.image.get_rect().center

        text_surf = self.font.render(
            self.attr["text"],
            True,
            self.attr["font_color"]
        )
        text_surf_hover = self.font.render(
            self.attr["text"],
            True,
            self.attr["font_color_hover"]
        )
        text_surf_down  = self.font.render(
            self.attr["text"],
            True,
            self.attr["font_color_down"]
        )
        text_surf_disabled  = self.font.render(
            self.attr["text"],
            True,
            self.attr["font_color_disabled"]
        )
        
        text_rect = text_surf.get_rect(center=(
            image_center_x,
            image_center_y
        ))
        
        self.surf_images["image_normal"].blit(text_surf, text_rect)
        self.surf_images["image_hover"].blit(text_surf_hover, text_rect)
        self.surf_images["image_down"].blit(text_surf_hover, text_rect)
        self.surf_images["image_disabled"].blit(text_surf_disabled, text_rect)
        
        self.button_down = False
        
    def set_attr(self, attributes):
        """Sets one or multiple attributes of the button.
        
        :param attributes: contains one or more attributes
        :type attributes: dict or tuple
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> a = mpos.forms.button.Button()
        >>> args = {"width": 100, "height": 20}
        >>> a.set_attr(args)
        >>> a.set_attr(("pos_x", 20))
        
        """
        return mpos.helpers.attr.set_attr(self.attr, attributes)

    def get_attr(self, key=None):
        """Sets one or multiple attributes of the button.
        
        :param attributes: contains one or more attributes
        :type attributes: dict or tuple
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> a = mpos.forms.button.Button()
        >>> all_attr = a.get_attr()
        >>> single_attr = a.get_attr("pos_x")
        
        """
        return mpos.helpers.attr.get_attr(self.attr, key)
            
    def update(self):
        """Updates button by its attributes.
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> a = mpos.forms.button.Button()
        >>> a.update()
        
        """
        self.rect.top = self.attr["pos_y"]
        self.rect.left = self.attr["pos_x"]
        
    def get_events(self):
        """Returns all button events and clears event queue.
        
        :returns: button event queue
        :rtype: list
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> a = mpos.forms.button.Button()
        >>> events = a.get_events()
        
        """
        return self.events
        
    def clear_events(self):
        """Clears the event queue of the button.
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> a = mpos.forms.button.Button()
        >>> a.clear_events()
        
        """
        self.events.clear()
    
    def handle_event(self, event):
        """Handles a single event.
                
        :param event: event that is to be handled by button
        :type event: pygame.event.Event
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> a = mpos.forms.button.Button()
        >>> for event in pygame.event.get(): a.handle_event(event)
        
        """
        if self.attr["clickable"]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.image = self.surf_images["image_down"]
                    self.button_down = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos) and self.button_down:
                    if self.attr["callback_event"] is not None:
                        self.events.append(self.attr["callback_event"])
                    self.image = self.surf_images["image_hover"]
                self.button_down = False
            elif event.type == pygame.MOUSEMOTION:
                collided = self.rect.collidepoint(event.pos)
                if collided and not self.button_down:
                    self.image = self.surf_images["image_hover"]
                elif not collided:
                    self.image = self.surf_images["image_normal"]
        else:
            self.image = self.surf_images["image_disabled"]
            
    def get_dimensions(self):
        """Returns the dimension of the button.
        
        :returns: button width and height
        :rtype: tuple
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> a = mpos.forms.button.Button()
        >>> events = a.get_dimensions()
        
        """
        return self.image.get_size()
        
    def width(self):
        """Returns the width of the button.
        
        :returns: button width
        :rtype: int
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> a = mpos.forms.button.Button()
        >>> events = a.width()
        
        """
        return self.image.get_width()
        
    def height(self):
        """Returns the height of the button.
        
        :returns: button height
        :rtype: int
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> a = mpos.forms.button.Button()
        >>> events = a.height()
        
        """
        return self.image.get_height()
