#########################################
# MPoS - just a library for development #
#########################################

### IMPORTS & INITIALISATON

from mpos.helpers.logger import log
import pygame

### CONSTANTS

### GLOBALS

### CLASSES & FUNCTIONS

class Button(pygame.sprite.Sprite):
    
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
            "img":              "assets/sprites/button.png",
            "img-hover":        "assets/sprites/button-clicked.png",
            "img-down":         "assets/sprites/button-clicked.png",
            "img-disabled":     "assets/sprites/button-disabled.png",
            "text-font":        "assets/fonts/Cinzel-Medium.ttf",
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
            logger.info("Button().set_attr(): Wrong format of given attributes")
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
            
    def update(self):
        
        # update position
        self.rect.top = self.attr["pos-y"]
        self.rect.left = self.attr["pos-x"]
        
    def get_events(self):
        return self.events
        
    def clear_events(self):
        
        # cleaning own event queue
        self.events.clear()
    
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
            
    def get_dimensions(self):
        return self.image.get_size()
