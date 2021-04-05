import pygame
import mpos.map.fields
import mpos.helpers.spritesheet

class Sector():
    
    def __init__(self, field_list, field_dict, size, field_size, spritesheet):
        
        self.field_list = field_list
        self.field_dict = field_dict
        self.field_size = field_size
        
        self.surface = pygame.Surface(size)
        
        self.spritesheet = spritesheet
        
        self.bg_color = (1, 0, 0)
        self.colorkey = (1, 0, 0)
        
        self.fields = pygame.sprite.Group()
        
        self.build_sector()
        
    def build_sector(self):
        
        pos_x = 0
        pos_y = 0
        
        for field_strip in self.field_list["fields"]:
            for field in field_strip:
                
                attr = self.field_dict[field]
                attr['size'] = (self.field_size, self.field_size)
                attr['sprite'] = self.spritesheet.image_at((attr['sprite_id']*self.field_size[0], 0, self.field_size[0], self.field_size[0]))
                attr['pos_x'] = pos_x
                attr['pos_y'] = pos_y
                if attr['sprite_rotation'] is not 0:
                    attr['sprite'] = self.spritesheet.image_rotate(
                        attr['sprite'], 
                        attr['sprite_rotation']
                    )
                new_f = mpos.map.fields.Field(attr)
                
                self.fields.add(new_f)
                
                pos_y += self.field_size[0]
                
            pos_x += self.field_size[0]
            pos_y = 0
        
    def render(self, surface, position):
        
        self.surface.fill(self.bg_color)
        
        if self.colorkey is not None:
            self.surface.set_colorkey(self.colorkey)
            
        self.fields.draw(self.surface)
        
        pygame.Surface.blit(
            surface,
            self.surface,
            position
        )
