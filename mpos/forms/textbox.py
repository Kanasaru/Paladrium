"""This module contains constants, functions and classes for
mpos.forms.textbox handling

:class Textbox: creates a textbox

.. note:: exports no objects
.. note:: raises no own exceptions

"""
import pygame
import mpos.msg
from mpos.helpers.logger import log

MODUL = __name__

class Textbox(pygame.sprite.Sprite):
    """This class provides and manages the general textbox of
    mpos.forms.textbox that can be added to a title.
    
    :method __init__: sets up the basic textbox
    :method set_attr: sets one or multiple textbox attributes
    :method get_attr: returns textbox attribute(s)
    :method update: updates textbox by own attributes values
    :method get_events: returns all events
    :method clear_events: clears the event list
    :method handle_event: handles an event
    :method get_dimensions: returns textbox size
    :method width: returns textbox width
    :method height: returns textbox height
    
    """
    def __init__(self, attributes=None):
        """Sets up the basic textbox.
        
        :param attributes: contains settings of the textbox
        :type attributes: dict
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> b = mpos.forms.textbox.Textbox()
        >>> args = {"width": 100, "height": 20}
        >>> a = mpos.forms.textbox.Textbox(args)
        
        """
        self.NAME = self.__class__.__name__
        
        pygame.sprite.Sprite.__init__(self)
        
        self.events = []
        self.attr = {
            "pos_x": 0,
            "pos_y": 0,
            "text": "Textbox",
            "text_font": None,
            "font_size": 20,
            "font_color": (255, 255, 255),
            "bg_color": (1, 0, 0),
            "colorkey": (1, 0, 0),
            "update_text_cb": None
        }
        if attributes is not None:
            self.set_attr(attributes)
        
        self.update()
        
    def set_attr(self, attributes):
        """Sets one or multiple attributes of the textbox.
        
        :param attributes: contains one or more attributes
        :type attributes: dict or tuple
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> a = mpos.forms.textbox.Textbox()
        >>> args = {"width": 100, "height": 20}
        >>> a.set_attr(args)
        >>> a.set_attr(("pos_x", 20))
        
        """
        if isinstance(attributes, tuple) and len(attributes) == 2:
            if attributes[0] in self.attr:
                self.attr[attributes[0]] = attributes[1]
            else:
                log.info(mpos.msg.echo(MODUL, self.NAME, mpos.msg.E_KEY))
                return False
        elif isinstance(attributes, dict):
            for key, value in attributes.items():
                if key in self.attr:
                    self.attr[key] = value
                else:
                    log.info(mpos.msg.echo(MODUL, self.NAME, mpos.msg.E_KEY))
        else:
            log.info(mpos.msg.echo(MODUL, self.NAME, mpos.msg.E_FORMAT))
            return False

        return True
        
    def get_attr(self, key=None):
        """Returns one or all attribute(s) of the textbox.
        
        :param key: key of attribute in dict
        :type key: str
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> a = mpos.forms.textbox.Textbox()
        >>> all_attr = a.get_attr()
        >>> single_attr = a.get_attr("pos_x")
        
        """
        if key is not None:
            if isinstance(key, str):
                if key in self.attr:
                    return self.attr[key]
                else:
                    log.info(mpos.msg.echo(MODUL, self.NAME, mpos.msg.E_KEY))
                    return False 
            else:
                log.info(mpos.msg.echo(MODUL, self.NAME, mpos.msg.E_KEYTYPE))
                return False
        else:
            return self.attr
            
    def update(self):
        """Updates textbox by its attributes.
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> a = mpos.forms.textbox.Textbox()
        >>> a.update()
        
        """
        if self.attr["update_text_cb"] is not None:
            self.attr["text"] = self.attr["update_text_cb"]()
            
        if self.attr["text_font"] is not None:
            self.font = pygame.font.Font(
                self.attr["text_font"],
                self.attr["font_size"]
            )
        else:
            self.font = pygame.font.Font(
                None,
                self.attr["font_size"]
            )
        text_width, text_height = self.font.size(self.attr["text"])
        
        self.image = pygame.Surface((text_width, text_height))
        self.image.fill(self.attr["bg_color"])
        self.image.set_colorkey(self.attr["colorkey"])
        
        self.rect = self.image.get_rect(topleft=(
            self.attr["pos_x"],
            self.attr["pos_y"]
        ))
        
        text_surf = self.font.render(
            self.attr["text"],
            True,
            self.attr["font_color"]
        )
        text_rect = text_surf.get_rect()
        
        self.image.blit(text_surf, text_rect)
        
        self.rect.top = self.attr["pos_y"]
        self.rect.left = self.attr["pos_x"]
        
    def get_events(self):
        """Returns all textbox events and clears event queue.
        
        :returns: textbox event queue
        :rtype: list
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> a = mpos.forms.textbox.Textbox()
        >>> events = a.get_events()
        
        """
        return self.events
        
    def clear_events(self):
        """Clears the event queue of the textbox.
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> a = mpos.forms.textbox.Textbox()
        >>> a.clear_events()
        
        """
        self.events.clear()
        
    def handle_event(self, event):
        """Handles a single event.
                
        :param event: event that is to be handled by textbox
        :type event: pygame.event.Event
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> a = mpos.forms.textbox.Textbox()
        >>> for event in pygame.event.get(): a.handle_event(event)
        
        """
        return
        
    def get_dimensions(self):
        """Returns the dimension of the textbox.
        
        :returns: textbox width and height
        :rtype: tuple
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> a = mpos.forms.textbox.Textbox()
        >>> events = a.get_dimensions()
        
        """
        return self.image.get_size()
        
    def width(self):
        """Returns the width of the textbox.
        
        :returns: textbox width
        :rtype: int
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> a = mpos.forms.textbox.Textbox()
        >>> events = a.width()
        
        """
        return self.image.get_width()
        
    def height(self):
        """Returns the height of the textbox.
        
        :returns: textbox height
        :rtype: int
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> a = mpos.forms.textbox.Textbox()
        >>> events = a.height()
        
        """
        return self.image.get_height()
