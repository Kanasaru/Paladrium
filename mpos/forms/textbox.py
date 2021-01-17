#########################################
# MPoS - just a library for development #
#########################################

### IMPORTS & INITIALISATON

from mpos.helpers.logger import log
import pygame

### CONSTANTS

### GLOBALS

### CLASSES & FUNCTIONS

class Textbox(pygame.sprite.Sprite):
    
    def __init__(self, attributes=None):
        # init parent
        pygame.sprite.Sprite.__init__(self)
        
        # creating empty event queue
        self.events = []
        
        # set attributes standard
        self.attr = {
            "pos-x":            0,
            "pos-y":            0,
            "text":             "",
            "text-font":        "assets/fonts/Cinzel-Medium.ttf",
            "text-size":        20,
            "text-color":       (255, 255, 255)
        }
        
        # override attributes
        if attributes is not None:
            self.set_attr(attributes)
        
        # load font
        self.font = pygame.font.Font(self.attr["text-font"], self.attr["text-size"])

        # create image by font size
        text_width, text_height = self.font.size(self.attr["text"])
        self.image = pygame.Surface((text_width, text_height))
        self.image.set_colorkey((0, 0, 0))
        
        # draw text into center
        self.rect = self.image.get_rect(topleft=(self.attr["pos-x"], self.attr["pos-y"]))
        
        text_surf = self.font.render(self.attr["text"], True, self.attr["text-color"])
        text_rect = text_surf.get_rect()
        
        # blit text onto image
        self.image.blit(text_surf, text_rect)
        
    def set_attr(self, attributes):
        
        # single attribute given?
        if isinstance(attributes, tuple) and len(attributes) == 2:
            if attributes[0] in self.attr:
                self.attr[attributes[0]] = attributes[1]
            else:
                log.info("Button().set_attr(): Given key does not exist in attributes")
                return False
                
        # multiple attributes given?
        elif isinstance(attributes, dict):
            for key, value in attributes.items():
                if key in self.attr:
                    self.attr[key] = value
                else:
                    log.info("Button().set_attr(): Given key from keys does not exist in attributes")
        else:
            log.info("Button().set_attr(): Wrong format of given attributes")
            return False

        return True
        
    def get_attr(self, key=None):
        
        # key is given
        if key is not None:
            if isinstance(key, str):
                if key in self.attr:
                    return self.attr[key]
                else:
                    log.info("Button().get_attr(): Given key does not exist in attributes")
                    return False 
            else:
                log.info("Button().get_attr(): Wrong type of given key")
                return False
        # no key? give them all we got
        else:
            return self.attr
            
    def get_events(self):
        return self.events
        
    def clear_events(self):
        
        # cleaning own event queue
        self.events.clear()
        
    def update(self):
        
        # update position
        self.rect.top = self.attr["pos-y"]
        self.rect.left = self.attr["pos-x"]
        
    def handle_event(self, event):
        
        # nothing to do for just text
        return
        
    def get_dimensions(self):
        return self.image.get_size()
        
    def width(self):
        return self.image.get_width()
        
    def height(self):
        return self.image.get_height()
        