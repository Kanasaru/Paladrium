#########################################
# MPoS - just a library for development #
#########################################

### IMPORTS & INITIALISATON

from mpos.helpers.logger import log
import pygame

### CONSTANTS

### GLOBALS

### CLASSES & FUNCTIONS

class Title():
    
    def __init__(self, attributes=None):
        
        # set attributes standard
        self.attr = {
            "pos_x":            0,
            "pos_y":            0,
            "width":            0,
            "height":           0,
            "text":             "",
            "text_font":        "assets/fonts/Cinzel-Medium.ttf",
            "font_size":        20,
            "font_color":       (0, 0 ,0),
            "background_color": (255, 255, 255),
            "colorkey":         None,
            "transparency":     255
        }
            
        # override attributes
        if attributes is not None:
            self.set_attr(attributes)
            
        # setup title surface
        self.surface = pygame.Surface((self.attr["width"], self.attr["height"]))
        
        # collecting all sprites of title in a group
        self.all_sprites = pygame.sprite.Group()
        
        # creating empty title event queue
        self.events = []
        
    def set_attr(self, attributes):
        
        # single attribute given?
        if isinstance(attributes, tuple) and len(attributes) == 2:
            if attributes[0] in self.attr:
                self.attr[attributes[0]] = attributes[1]
            else:
                log.info("Title().set_attr(): Given key does not exist in attributes")
                return False
                
        # multiple attributes given?
        elif isinstance(attributes, dict):
            for key, value in attributes.items():
                if key in self.attr:
                    self.attr[key] = value
                else:
                    log.info("Title().set_attr(): Given key from keys does not exist in attributes")
        else:
            log.info("Title().set_attr(): Wrong format of given attributes")
            return False

        return True
        
    def get_attr(self, key=None):
        
        # key is given
        if key is not None:
            if isinstance(key, str):
                if key in self.attr:
                    return self.attr[key]
                else:
                    log.info("Title().get_attr(): Given key does not exist in attributes")
                    return False 
            else:
                log.info("Title().get_attr(): Wrong type of given key")
                return False
        # no key? give them all we got
        else:
            return self.attr
            
    def add(self, form_object):
        
        self.all_sprites.add(form_object)
        
    def get_events(self):
        
        # collect all events raised by forms objects in sprite group
        for form_object in self.all_sprites:
            self.events.extend(form_object.get_events())
            
            # cleaning forms object event queue
            form_object.clear_events()

        return self.events
        
    def clear_events(self):
        
        # cleaning own event queue
        self.events.clear()
        
    def handle_event(self, event):
        
        # call event handler of every forms object in sprite group
        for form_object in self.all_sprites:
            form_object.handle_event(event)
            
    def run_logic(self):
        
        # update every forms object in sprite group
        self.all_sprites.update()
        
    def render(self, surface):
        
        # fill display with background color
        self.surface.fill(self.attr["background_color"])
        
        if self.attr["colorkey"] is not None:
            self.surface.set_colorkey(self.attr["colorkey"])
        
        self.surface.set_alpha(self.attr["transparency"])
        
        # draw every forms object in sprite group
        self.all_sprites.draw(self.surface)
        
        pygame.Surface.blit(surface, self.surface, (self.attr["pos_x"], self.attr["pos_y"]))
