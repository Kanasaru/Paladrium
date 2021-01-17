#########################################
# MPoS - just a library for development #
#########################################

### IMPORTS & INITIALISATON

import pygame

import mpos.helpers.time
from mpos.helpers.logger import log

### CONSTANTS

QUIET      = 0
LOUD       = 1

### GLOBALS

### CLASSES & FUNCTIONS
        
class DebugScreen():
    
    def __init__(self, attributes=None):
        
        # set attributes standard
        self.attr = {
            "pos_x":            0,
            "pos_y":            0,
            "width":            0,
            "height":           0,
            "text_font":        "assets/fonts/RobotoMono-VariableFont_wght.ttf",
            "font_size":        14,
            "font_color":       (0, 0 ,0),
            "background_color": (255, 255, 255),
            "colorkey":         None,
            "transparency":     60,
            "mode":             QUIET
        }
            
        # override attributes
        if attributes is not None:
            self.set_attr(attributes)
        
        # collecting all sprites of title in a group
        self.all_sprites = pygame.sprite.Group()
        
        self.add(DebugTimer())
        
    def set_attr(self, attributes):
        
        # single attribute given?
        if isinstance(attributes, tuple) and len(attributes) == 2:
            if attributes[0] in self.attr:
                self.attr[attributes[0]] = attributes[1]
            else:
                log.info("Debugger().set_attr(): Given key does not exist in attributes")
                return False
                
        # multiple attributes given?
        elif isinstance(attributes, dict):
            for key, value in attributes.items():
                if key in self.attr:
                    self.attr[key] = value
                else:
                    log.info("Debugger().set_attr(): Given key from keys does not exist in attributes")
        else:
            log.info("Debugger().set_attr(): Wrong format of given attributes")
            return False

        return True
        
    def get_attr(self, key=None):
        
        # key is given
        if key is not None:
            if isinstance(key, str):
                if key in self.attr:
                    return self.attr[key]
                else:
                    log.info("Debugger().get_attr(): Given key does not exist in attributes")
                    return False 
            else:
                log.info("Debugger().get_attr(): Wrong type of given key")
                return False
        # no key? give them all we got
        else:
            return self.attr
            
    def toggle(self):
        
        if self.attr["mode"] == LOUD:
            self.attr["mode"] = QUIET
        else:
            self.attr["mode"] = LOUD
            
    def set_mode(self, mode):
        
        if mode == QUIET:
            self.attr["mode"] = QUIET
        elif mode == LOUD:
            self.attr["mode"] = LOUD
        else:
            log.info("Unknown mode for debugging")
            mode = QUIET
        
    def get_mode(self):
        
        return self.attr["mode"]
            
    def is_mode(self, mode):
        
        if mode == self.attr["mode"]:
            return True
        else:
            return False
            
    def add(self, sprite):
        
        self.all_sprites.add(sprite)
        
    def handle_event(self, event):
        return
            
    def run_logic(self):
        
        self.all_sprites.update()
        
    def render(self, surface):
        
        if self.attr["mode"] == LOUD:
        
            self.surface = pygame.Surface((self.attr["width"], self.attr["height"]))
            
            self.surface.fill(self.attr["background_color"])
            
            if self.attr["colorkey"] is not None:
                self.surface.set_colorkey(self.attr["colorkey"])
            
            self.surface.set_alpha(self.attr["transparency"])
            
            self.all_sprites.draw(self.surface)
            
            pygame.Surface.blit(surface, self.surface, (self.attr["pos_x"], self.attr["pos_y"]))
        
        
class DebugTimer(pygame.sprite.Sprite):
    
    def __init__(self, attributes=None):
        
        # init parent
        pygame.sprite.Sprite.__init__(self)
        
        self.timer = pygame.time.get_ticks()
        
        # creating empty event queue
        self.events = []
        
        # set attributes standard
        self.attr = {
            "pos_x":            0,
            "pos_y":            0,
            "text":             "DebugTimer: ",
            "timer":            self.get_time(),
            "text_font":        "assets/fonts/BungeeShade-Regular.ttf",
            "font_size":        20,
            "font_color":       (255, 255, 255)
        }
        
        # override attributes
        if attributes is not None:
            self.set_attr(attributes)
        
        # load font
        self.font = pygame.font.Font(self.attr["text_font"], self.attr["font_size"])

        self.create_sprite()
        
    def create_sprite(self):
        
        text = self.attr["text"] + self.attr["timer"]
        
        # create image by font size
        text_width, text_height = self.font.size(text)
        self.image = pygame.Surface((text_width, text_height))
        self.image.set_colorkey((0, 0, 0))
        # draw text into center
        self.rect = self.image.get_rect(topleft=(self.attr["pos_x"], self.attr["pos_y"]))
        
        text_surf = self.font.render(text, True, self.attr["font_color"])
        text_rect = text_surf.get_rect(center=self.rect.center)
        
        # blit text onto image
        self.image.blit(text_surf, text_rect)
        
        
    def get_time(self):
        time_diff = pygame.time.get_ticks()-self.timer
        seconds = time_diff//1000
        
        return mpos.helpers.time.seconds_to_clock(seconds)
    
    def update(self):
        
        self.attr["timer"] = self.get_time()
        self.create_sprite()
        
    def get_events(self):
        return self.events
        
    def clear_events(self):
        
        # cleaning own event queue
        self.events.clear()
        
    def handle_event(self, event):
        return
        
    def get_dimensions(self):
        return self.image.get_size()
        