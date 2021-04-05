import pygame
import mpos.msg
import mpos.helpers.attr
from mpos.helpers.logger import log

MODUL = __name__

class Field(pygame.sprite.Sprite):
    def __init__(self, attributes=None):
        self.NAME = self.__class__.__name__
        
        pygame.sprite.Sprite.__init__(self)
        
        self.attr = {
            "pos_x": 0,
            "pos_y": 0,
            "size": (32, 32),
            "name": None,
            "accessable": True,
            "fluid": False,
            "damage": 0,
            "bg_color": (100, 100, 100),
            "sprite": None,
            "sprite_id": 0,
            "sprite_rotation": 0
        }
        if attributes is not None:
            self.set_attr(attributes)
        
        self.image = self.attr["sprite"]
        
        self.rect = self.image.get_rect(topleft=(
            self.attr["pos_y"],
            self.attr["pos_x"]
        ))
        
    def set_attr(self, attributes):
        return mpos.helpers.attr.set_attr(self.attr, attributes)
        
    def get_attr(self, key=None):
        return mpos.helpers.attr.get_attr(self.attr, key)
            
    def update(self):
        return
