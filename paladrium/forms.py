#########################################
# Paladrium - a RPG Project             #
# https://github.com/Kanasaru/Paladrium #
# GPL 3.0 License                       #
#########################################


### IMPORTS & INITIALISATON

import pygame

from . import debug
from . import events

### CONSTANTS


### CLASSES & FUNCTIONS

##
# Class: Title()
# Parent: none
##
class Title():
    
    ##
    # Method: __init__
    # Class: Title()
    # @param: (tuple) bg_color
    # @return: none
    ##
    def __init__(self, resolution, bg_color, position=(0, 0), transparent=255):
        
        # set title surface
        self.surface = pygame.Surface(resolution)
        self.surface.set_alpha(transparent)
        self.position = position
        
        # set title background color
        self.bg_color = bg_color
        
        # collecting all sprites of title in a group
        self.all_sprites = pygame.sprite.Group()
        
        # creating empty title event queue
        self.events = []
        
    ##
    # Method: add
    # Class: Title()
    # @param: (forms object) form_object
    # @return: none
    ##
    def add(self, form_object):
        
        # check if given forms object is allowed and add it to sprite group
        if isinstance(form_object, Button):
            self.all_sprites.add(form_object)
        elif isinstance(form_object, Textfield):
            self.all_sprites.add(form_object)
        elif isinstance(form_object, Text):
            self.all_sprites.add(form_object)
        else:
            debug.Debug.msg("Title().add(): Given type is not allowed")
            
    ##
    # Method: get_events
    # Class: Title()
    # @param: none
    # @return: (list) self.events
    ##
    def get_events(self):
        
        # collect all events raised by forms objects in sprite group
        for form_object in self.all_sprites:
            self.events.extend(form_object.get_events())
            
            # cleaning forms object event queue
            form_object.clear_events()

        return self.events
        
    ##
    # Method: clear_events
    # Class: Title()
    # @param: none
    # @return: none
    ##
    def clear_events(self):
        
        # cleaning own event queue
        self.events.clear()
        
    ##
    # Method: handle_event
    # Class: Title()
    # @param: (events.Event) event
    # @return: none
    ##
    def handle_event(self, event):
        
        # call event handler of every forms object in sprite group
        for form_object in self.all_sprites:
            form_object.handle_event(event)
            
    ##
    # Method: run_logic
    # Class: Title()
    # @param: none
    # @return: none
    ##
    def run_logic(self):
        
        # update every forms object in sprite group
        self.all_sprites.update()
        
    ##
    # Method: render
    # Class: Title()
    # @param: none
    # @return: none
    ##
    def render(self):
        
        # fill display with background color
        self.surface.fill(self.bg_color)
        
        # draw every forms object in sprite group
        self.all_sprites.draw(self.surface)
        
        pygame.Surface.blit(pygame.display.get_surface(), self.surface, self.position)
        
        
##
# Class: Button()
# Parent: pygame.sprite.Sprite
##
class Button(pygame.sprite.Sprite):
    
    ##
    # Method: __init__
    # Class: Button()
    # @param: (tuple) bg_color
    # @return: none
    ##
    def __init__(self, attributes=None):
        
        # init parent
        pygame.sprite.Sprite.__init__(self)
        
        # creating empty event queue
        self.events = []
        
        # set attributes standard
        self.attr = {
            "pos-x":            0,
            "pos-y":            0,
            "width":            220,
            "height":           60,
            "text":             "",
            "callback_event":   None,
            "clickable":        True,
            "img":              "assets/button.png",
            "img-hover":        "assets/button-clicked.png",
            "img-down":         "assets/button-clicked.png",
            "img-disabled":     "assets/button-disabled.png",
            "text-font":        "assets/Cinzel-Medium.ttf",
            "text-size":        20,
            "text-color":       (0, 0 ,0),
            "text-color-hover": (120, 117, 98),
            "text-color-down":  (120, 117, 98),
            "shadow":           (0, 0)
        }
        
        # override attributes
        if attributes is not None:
            self.set_attr(attributes)
        
        # load font
        self.font = pygame.font.Font(self.attr["text-font"], self.attr["text-size"])
        
        # load button images and convert alpha
        self.image_normal   = pygame.image.load(self.attr["img"]).convert_alpha()
        self.image_hover    = pygame.image.load(self.attr["img-hover"]).convert_alpha()
        self.image_down     = pygame.image.load(self.attr["img-down"]).convert_alpha()
        self.image_disabled = pygame.image.load(self.attr["img-disabled"]).convert_alpha()
        
        # scale button images to given button size
        self.image_normal   = pygame.transform.scale(self.image_normal, (self.attr["width"], self.attr["height"]))
        self.image_hover    = pygame.transform.scale(self.image_hover, (self.attr["width"], self.attr["height"]))
        self.image_down     = pygame.transform.scale(self.image_down, (self.attr["width"], self.attr["height"]))
        self.image_disabled = pygame.transform.scale(self.image_disabled, (self.attr["width"], self.attr["height"]))

        # set current image
        if self.attr["clickable"]:
            self.image = self.image_normal
        else:
            self.image = self.image_disabled
        
        # set rect
        self.rect = self.image.get_rect(topleft=(self.attr["pos-y"], self.attr["pos-x"]))
        
        # draw text into center
        image_center_x, image_center_y = self.image.get_rect().center

        text_surf       = self.font.render(self.attr["text"], True, self.attr["text-color"])
        text_surf_hover = self.font.render(self.attr["text"], True, self.attr["text-color-hover"])
        text_surf_down  = self.font.render(self.attr["text"], True, self.attr["text-color-down"])
        
        # set text rect with shadow
        shadow = self.attr["shadow"]
        
        text_rect = text_surf.get_rect(center=(image_center_x - shadow[1], image_center_y - shadow[0]))
        
        # blit text onto images
        self.image_normal.blit(text_surf, text_rect)
        self.image_hover.blit(text_surf_hover, text_rect)
        self.image_down.blit(text_surf_hover, text_rect)
        self.image_disabled.blit(text_surf, text_rect)
        
        # set current button state
        self.button_down = False
        
    ##
    # Method: set_attr
    # Class: Button()
    # @param: (tuple) (dict) attributes
    # @return: (bool)
    ##
    def set_attr(self, attributes):
        
        # single attribute given?
        if isinstance(attributes, tuple) and len(attributes) == 2:
            if attributes[0] in self.attr:
                self.attr[attributes[0]] = attributes[1]
            else:
                debug.Debug.msg("Button().set_attr(): Given key does not exist in attributes")
                return False
                
        # multiple attributes given?
        elif isinstance(attributes, dict):
            for key, value in attributes.items():
                if key in self.attr:
                    self.attr[key] = value
                else:
                    debug.Debug.msg("Button().set_attr(): Given key from keys does not exist in attributes")
        else:
            debug.Debug.msg("Button().set_attr(): Wrong format of given attributes")
            return False

        return True

    ##
    # Method: set_attr
    # Class: Button()
    # @param: (optional) (str) key
    # @return: (mixed) (dict) (bool)
    ##
    def get_attr(self, key=None):
        
        # key is given
        if key is not None:
            if isinstance(key, str):
                if key in self.attr:
                    return self.attr[key]
                else:
                    debug.Debug.msg("Button().get_attr(): Given key does not exist in attributes")
                    return False 
            else:
                debug.Debug.msg("Button().get_attr(): Wrong type of given key")
                return False
        # no key? give them all we got
        else:
            return self.attr
            
    ##
    # Method: update
    # Class: Button()
    # @param: none
    # @return: none
    ##
    def update(self):
        
        # update position
        self.rect.top = self.attr["pos-y"]
        self.rect.left = self.attr["pos-x"]
        
    ##
    # Method: get_events
    # Class: Button()
    # @param: none
    # @return: (list) self.events
    ##
    def get_events(self):
        return self.events
        
    ##
    # Method: clear_events
    # Class: Button()
    # @param: none
    # @return: none
    ##
    def clear_events(self):
        
        # cleaning own event queue
        self.events.clear()
    
    ##
    # Method: handle_event
    # Class: Button()
    # @param: (events.Event) event
    # @return: none
    ##
    def handle_event(self, event):
        
        # just handle events if button is clickable
        if self.attr["clickable"]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.image = self.image_down
                    self.button_down = True
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos) and self.button_down:
                    # raise the callback event if it has one
                    if self.attr["callback_event"] is not None:
                        self.events.append(self.attr["callback_event"])
                    
                    self.image = self.image_hover
                self.button_down = False
                
            elif event.type == pygame.MOUSEMOTION:
                collided = self.rect.collidepoint(event.pos)
                if collided and not self.button_down:
                    self.image = self.image_hover
                elif not collided:
                    self.image = self.image_normal
                    
        # not clickable? tell the crowd
        else:
            self.image = self.image_disabled
            
    ##
    # Method: get_dimensions
    # Class: Button()
    # @param: none
    # @return: (tuple)
    ##
    def get_dimensions(self):
        return self.image.get_size()
            
##
# Class: Textfield()
# Parent: pygame.sprite.Sprite()
##
class Textfield(pygame.sprite.Sprite):
    
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
            "text-font":        "assets/Cinzel-Medium.ttf",
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
        self.rect = self.image.get_rect(topleft=(self.attr["pos-x"] - text_width / 2, self.attr["pos-y"]))
        
        text_surf = self.font.render(self.attr["text"], True, self.attr["text-color"])
        text_rect = text_surf.get_rect()
        
        # blit text onto image
        self.image.blit(text_surf, text_rect)
        
    ##
    # Method: set_attr
    # Class: Textfield()
    # @param: (tuple) (dict) attributes
    # @return: (bool)
    ##
    def set_attr(self, attributes):
        
        # single attribute given?
        if isinstance(attributes, tuple) and len(attributes) == 2:
            if attributes[0] in self.attr:
                self.attr[attributes[0]] = attributes[1]
            else:
                debug.Debug.msg("Button().set_attr(): Given key does not exist in attributes")
                return False
                
        # multiple attributes given?
        elif isinstance(attributes, dict):
            for key, value in attributes.items():
                if key in self.attr:
                    self.attr[key] = value
                else:
                    debug.Debug.msg("Button().set_attr(): Given key from keys does not exist in attributes")
        else:
            debug.Debug.msg("Button().set_attr(): Wrong format of given attributes")
            return False

        return True

    ##
    # Method: set_attr
    # Class: Textfield()
    # @param: (optional) (str) key
    # @return: (mixed) (dict) (bool)
    ##
    def get_attr(self, key=None):
        
        # key is given
        if key is not None:
            if isinstance(key, str):
                if key in self.attr:
                    return self.attr[key]
                else:
                    debug.Debug.msg("Button().get_attr(): Given key does not exist in attributes")
                    return False 
            else:
                debug.Debug.msg("Button().get_attr(): Wrong type of given key")
                return False
        # no key? give them all we got
        else:
            return self.attr
            
    ##
    # Method: get_events
    # Class: Textfield()
    # @param: none
    # @return: (list) self.events
    ##
    def get_events(self):
        return self.events
        
    ##
    # Method: clear_events
    # Class: Textfield()
    # @param: none
    # @return: none
    ##
    def clear_events(self):
        
        # cleaning own event queue
        self.events.clear()
        
    ##
    # Method: handle_event
    # Class: Textfield()
    # @param: (events.Event) event
    # @return: none
    ##
    def handle_event(self, event):
        
        # nothing to do for just text
        return
        
    ##
    # Method: get_dimensions
    # Class: Textfield()
    # @param: none
    # @return: (tuple)
    ##
    def get_dimensions(self):
        return self.image.get_size()

##
# Class: Textfield()
# Parent: pygame.sprite.Sprite()
##
class Text(pygame.sprite.Sprite):
    
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
            "text-font":        "assets/Cinzel-Medium.ttf",
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
        
    ##
    # Method: set_attr
    # Class: Textfield()
    # @param: (tuple) (dict) attributes
    # @return: (bool)
    ##
    def set_attr(self, attributes):
        
        # single attribute given?
        if isinstance(attributes, tuple) and len(attributes) == 2:
            if attributes[0] in self.attr:
                self.attr[attributes[0]] = attributes[1]
            else:
                debug.Debug.msg("Button().set_attr(): Given key does not exist in attributes")
                return False
                
        # multiple attributes given?
        elif isinstance(attributes, dict):
            for key, value in attributes.items():
                if key in self.attr:
                    self.attr[key] = value
                else:
                    debug.Debug.msg("Button().set_attr(): Given key from keys does not exist in attributes")
        else:
            debug.Debug.msg("Button().set_attr(): Wrong format of given attributes")
            return False

        return True

    ##
    # Method: set_attr
    # Class: Textfield()
    # @param: (optional) (str) key
    # @return: (mixed) (dict) (bool)
    ##
    def get_attr(self, key=None):
        
        # key is given
        if key is not None:
            if isinstance(key, str):
                if key in self.attr:
                    return self.attr[key]
                else:
                    debug.Debug.msg("Button().get_attr(): Given key does not exist in attributes")
                    return False 
            else:
                debug.Debug.msg("Button().get_attr(): Wrong type of given key")
                return False
        # no key? give them all we got
        else:
            return self.attr
            
    ##
    # Method: get_events
    # Class: Textfield()
    # @param: none
    # @return: (list) self.events
    ##
    def get_events(self):
        return self.events
        
    ##
    # Method: clear_events
    # Class: Textfield()
    # @param: none
    # @return: none
    ##
    def clear_events(self):
        
        # cleaning own event queue
        self.events.clear()
        
    ##
    # Method: handle_event
    # Class: Textfield()
    # @param: (events.Event) event
    # @return: none
    ##
    def handle_event(self, event):
        
        # nothing to do for just text
        return
        
    ##
    # Method: get_dimensions
    # Class: Textfield()
    # @param: none
    # @return: (tuple)
    ##
    def get_dimensions(self):
        return self.image.get_size()
        