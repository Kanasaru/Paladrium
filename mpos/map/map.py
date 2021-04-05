import pygame
import math

class Map():
    
    def __init__(self, map_dict, field_dict, resolution, spritesheet, field_size=(32, 32)):
        
        self.NAME = self.__class__.__name__
        
        self.map_dict = map_dict
        self.field_dict = field_dict
        self.bg_color = (0, 0, 0)
        self.colorkey = None
        
        self.field_size = field_size
        
        self.surface = pygame.Surface(resolution)
        
        self.sector_size = (
            self.map_dict["sector_size"][0]*self.field_size[0],
            self.map_dict["sector_size"][1]*self.field_size[1],
        )
        
        self.spritesheet = mpos.helpers.spritesheet.SpriteSheet(
            spritesheet,
            self.field_size
        )
        
        self.position = self.set_position()
        
        self.current_sector = mpos.map.sectors.Sector(
            self.map_dict[0],
            self.field_dict,
            self.sector_size,
            self.field_size,
            self.spritesheet
        )
        
    def set_position(self):
        x = (self.surface.get_width() - self.sector_size[0]) / 2
        y = (self.surface.get_height() - self.sector_size[1]) / 2
        
        return (x, y)
        
    def run_logic(self):
        return
        
    def render(self, surface):
        
        self.surface.fill(self.bg_color)
        
        if self.colorkey is not None:
            self.surface.set_colorkey(self.colorkey)
            
        self.current_sector.render(self.surface, self.position)
        
        pygame.Surface.blit(
                surface,
                self.surface,
                (0, 0)
        )
