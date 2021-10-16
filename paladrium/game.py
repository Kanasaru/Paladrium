"""This module contains settings functionality

:class Game: manages the game

.. note:: https://github.com/Kanasaru/Paladrium

"""
import pygame
pygame.init()
import mpos
import paladrium.titles
from paladrium.logger import log
from paladrium.settings import settings
from paladrium.map.map import MAP_DICT
from paladrium.map.fields import FIELD_DICT

class Game():
    """This class manages the game.
    
    :method __init__: sets up the game
    :method loop: starts the gaming loop
    :method handle_events: handles game events
    :method run_logic: runs all game logic
    :method render: draws everything onto pygame display
    :method exit: controls an exit
    
    """
    def __init__(self):
        """
        Sets up the game.
        """
        self.game_running = False
        self.exit_game = False
        self.new_title = None
        self.resolution_update = None
        self.debugger = mpos.helpers.debug.Debugger()
        
        attr = {
            "pos_x": 0,
            "pos_y": settings.get_display_resolution(False, True) - 100,
            "width": settings.get_display_resolution(True, False),
            "height": 100
        }
        self.debug_screen = mpos.forms.title.Title(attr)
        
        attr = {
            "text": self.debugger.get_str_timer(),
            "font_color": (0, 0, 0),
            "update_text_cb": getattr(self.debugger, 'get_str_timer')
        }
        self.debug_screen.add(mpos.forms.textbox.Textbox(attr))
        
        self.clock    = pygame.time.Clock()
        
        self.surface = pygame.display.set_mode(
            settings.get_display_resolution()
        )
        
        display_title = settings.get_game_title() + " - v"
        display_title += settings.get_game_version() + " by "
        display_title += settings.get_game_author()
        pygame.display.set_caption(display_title)
        
        settings.set_current_title(
            paladrium.titles.build_title(paladrium.titles.MAIN)
        )
        
        self.map = mpos.map.map.Map(
            MAP_DICT,
            FIELD_DICT,
            settings.get_display_resolution(),
            "assets/sprites/fields_spritesheet.png"
        )
        
        self.loop()
        
    def loop(self):
        """Starts the gaming loop."""
        while not self.exit_game:
            
            self.clock.tick(settings.get_fps())
            
            self.handle_events()
            self.run_logic()
            self.render()
            
        self.exit()
        
    def handle_events(self):
        """Handles game events."""
        if not self.game_running:
            for event in settings.get_current_title().get_events():
                if event.code == paladrium.events.NEWTITLE:
                    self.new_title = event.data
                elif event.code == paladrium.events.RESOLUTION:
                    self.resolution_update = event.data
                elif event.code == paladrium.events.STARTGAME:
                    self.game_running = True
                elif event.code == paladrium.events.QUITGAME:
                    self.exit_game = True
                log.info(event)
            settings.get_current_title().clear_events()
            
            for event in pygame.event.get():
                settings.get_current_title().handle_event(event)
                
                if event.type == pygame.QUIT:
                    self.exit_game = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_F3:
                        self.debugger.toggle()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game = True
                    log.info("PyGame QUIT")
            
    def run_logic(self):
        """Runs all game logic."""
        if not self.game_running:
            if self.resolution_update is not None:
                settings.set_display_resolution(self.resolution_update)
                pygame.display.set_mode(settings.get_display_resolution())
                settings.set_current_title(
                    paladrium.titles.build_title(paladrium.titles.RESOLUTION)
                )
                self.resolution_update = None
                
            if self.new_title is not None:
                settings.set_current_title(
                    paladrium.titles.build_title(self.new_title)
                )
                self.new_title = None
                
            settings.get_current_title().run_logic()
        else:
            self.map.run_logic()
            
        attr = {
            "pos_y": settings.get_display_resolution(False, True) - 100,
            "width": settings.get_display_resolution(True, False),
        }
        self.debug_screen.set_attr(attr)
        self.debug_screen.run_logic()
            
    def render(self):
        """Draws everything onto pygame display"""
        self.surface.fill((0, 255, 0))
        
        if not self.game_running:
            settings.get_current_title().render(self.surface)
        else:
            self.map.render(self.surface)
            
        if self.debugger.is_mode(mpos.helpers.debug.LOUD):
            self.debug_screen.render(self.surface)
            
        pygame.display.flip()
        
    def exit(self):
        """Controls an exit."""
        pygame.quit()
        
    def load_map(self):
        attr = {
            "pos_x": 0,
            "pos_y": 0,
            "width": settings.get_display_resolution(True, False),
            "height": settings.get_display_resolution(False, True),
            "bg_color": (0, 0, 255),
            "colorkey": (0, 0, 0)
        }
        self.map = paladrium.map.map.Map(self.map_file, attr)
