"""This module contains constants, functions and classes for
mpos.forms.title handling

:class Title: collects and manages mpos.forms objects

.. note:: exports no objects
.. note:: raises no exceptions

"""
import pygame
import mpos.msg
from mpos.helpers.logger import log

MODUL = __name__

class Title():
    """This class manages a PyGame surface and handles mpos.forms
    objects that are added to its instance.
    
    :method __init__: sets up the basic title
    :method set_attr: sets one or multiple attributes
    :method get_attr: returns attribute(s)
    :method add: adds an object of mpos.forms
    :method get_events: returns all events
    :method clear_events: clears the event list
    :method handle_event: handles an event
    :method run_logic: updates every object
    :method render: draws every object and the title itself
    
    """
    def __init__(self, attributes=None):
        """Sets up the basic title.
        
        :param attributes: contains settings
        :type attributes: dict
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> b = mpos.forms.title.Title()
        >>> args = {"width": 100, "height": 20}
        >>> a = mpos.forms.title.Title(args)
        
        """
        self.NAME = self.__class__.__name__
        
        self.attr = {
            "pos_x": 0,
            "pos_y": 0,
            "width": 0,
            "height": 0,
            "bg_color": (255, 255, 255),
            "colorkey": None
        }
        if attributes is not None:
            self.set_attr(attributes)
            
        self.surface = pygame.Surface((
            self.attr["width"],
            self.attr["height"]
        ))
        self.form_objects = pygame.sprite.Group()
        self.events = []
        
    def set_attr(self, attributes):
        """Sets one or multiple attributes.
        
        :param attributes: contains one or more attributes
        :type attributes: dict or tuple
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> a = mpos.forms.title.Title()
        >>> args = {"width": 100, "height": 20}
        >>> a.set_attr(args)
        >>> a.set_attr(("pos_x", 20))
        
        """
        if isinstance(attributes, tuple) and len(attributes) == 2:
            if attributes[0] in self.attr:
                self.attr[attributes[0]] = attributes[1]
            else:
                log.info(mpos.msg.echo(MODUL, self.NAME, self.E_KEY))
                return False
        elif isinstance(attributes, dict):
            for key, value in attributes.items():
                if key in self.attr:
                    self.attr[key] = value
                else:
                    log.info(mpos.msg.echo(MODUL, self.NAME, self.E_KEY))
        else:
            log.info(mpos.msg.echo(MODUL, self.NAME, self.E_FORMAT))
            return False

        return True
        
    def get_attr(self, key=None):
        """Returns one or all attribute(s)
        
        :param key: key of attribute in dict
        :type key: str
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> a = mpos.forms.title.Title()
        >>> all_attr = a.get_attr()
        >>> single_attr = a.get_attr("pos_x")
        
        """
        if key is not None:
            if isinstance(key, str):
                if key in self.attr:
                    return self.attr[key]
                else:
                    log.info(mpos.msg.echo(MODUL, self.NAME, self.E_KEY))
                    return False 
            else:
                log.info(mpos.msg.echo(MODUL, self.NAME, self.E_KEYTYPE))
                return False
        else:
            return self.attr
            
    def add(self, form_object):
        """Adds an object.
        
        :param form_object: form object
        :type form_object: pygame.sprite.Sprite
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> button = mpos.forms.button.Button()
        >>> a = mpos.forms.title.Title()
        >>> a.add(button)
        
        .. warning:: form_object needs to provide additional methods
            get_events()
            clear_events()
            handle_event(event)
        
        """
        self.form_objects.add(form_object)
        
    def get_events(self):
        """Returns all title events and clears event queue.
        
        :returns: titles event queue
        :rtype: list
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> a = mpos.forms.title.Title()
        >>> events = a.get_events()
        
        """
        for form_object in self.form_objects:
            self.events.extend(form_object.get_events())
            form_object.clear_events()

        return self.events
        
    def clear_events(self):
        """Clears the event queue.
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> a = mpos.forms.title.Title()
        >>> a.clear_events()
        
        """
        self.events.clear()
        
    def handle_event(self, event):
        """Handles an event through form objects and itself.
                
        :param event: event that is to be handled by title and objects
        :type event: pygame.event.Event
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> a = mpos.forms.title.Title()
        >>> for event in pygame.event.get(): a.handle_event(event)
        
        """
        for form_object in self.form_objects:
            form_object.handle_event(event)
            
    def run_logic(self):
        """Updates every object of the title and itself.
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> a = mpos.forms.title.Title()
        >>> a.run_logic()
        
        """
        self.form_objects.update()
        
    def render(self, surface):
        """Draws every object and the title itself onto given surface.
        
        :param surface: surface the title will blit
        :type surface: pygame.Surface
        
        :Example:
        
        >>> import pygame
        >>> import mpos.forms
        >>> pygame.init()
        >>> my_surface = pygame.Surface(100, 100)
        >>> a = mpos.forms.title.Title()
        >>> a.render(my_surface)
        
        """
        self.surface.fill(self.attr["bg_color"])
        if self.attr["colorkey"] is not None:
            self.surface.set_colorkey(self.attr["colorkey"])
        
        self.form_objects.draw(self.surface)
        
        pygame.Surface.blit(
            surface,
            self.surface,
            (self.attr["pos_x"], self.attr["pos_y"])
        )
