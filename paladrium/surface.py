#########################################
# Paladrium - a RPG Project             #
# https://github.com/Kanasaru/Paladrium #
# GPL 3.0 License                       #
#########################################

import pygame
from . import constants

##
# Class: Field (object pygame.sprite.Sprite)
# Object holds every information for one field
# Object contains functions to modify a field
##

class Field(pygame.sprite.Sprite):
    
    accessable = True
    
    def __init__(self, x, y, color):
        super().__init__()
 
        # set height, width
        self.image = pygame.Surface([constants.FIELDSIZE, constants.FIELDSIZE])
        self.image.fill(color)
 
        # set position by coordinates and size
        self.rect = self.image.get_rect()
        self.rect.y = y * constants.FIELDSIZE
        self.rect.x = x * constants.FIELDSIZE
        
    def setcolor(self, color):
        self.image.fill(color)

##
# Class: Sector ()
# Object holds a list of fields
##

class Sector(object):

    field_list = None
 
    def __init__(self):
        self.field_list = pygame.sprite.Group()

##
# Class: Sector1 ()
# Just a testing object. Will be replaced with map and sector loading.
##

class Sector1(Sector):
    def __init__(self):
        super().__init__()
        fields = [[0, 0, constants.WHITE],
                 [0, 1, constants.GREEN],
                 [1, 2, constants.BLUE]]
 
        for item in fields:
            field = Field(item[0], item[1], item[2])
            self.field_list.add(field)
