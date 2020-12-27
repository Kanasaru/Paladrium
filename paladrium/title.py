#########################################
# Paladrium - a RPG Project             #
# https://github.com/Kanasaru/Paladrium #
# GPL 3.0 License                       #
#########################################


### IMPORTS & INITIALISATON

# PyGame
import pygame

import os
from pathlib import Path

# Paladrium modules
from . import events


### CLASSES & FUNCTIONS

##
# Class: Title()
# Contains general methods for title screen handling
##

class Title():
    
    def __init__(self, screen, eventhandler, bg_color):
        # all title sprites are collected for rendering
        self.all_sprites = pygame.sprite.Group()
        # event handler instance
        self.eventhandler = eventhandler
        # main screen instance
        self.title_screen = screen
        # title background color
        self.bg_color = bg_color
        
    def handle_events(self):
        # check for typical title events
        for event in self.eventhandler.events:
            # buttons
            for button in self.all_sprites:
                button.handle_event(event)
            # TODO: mouse and key events
    
    def run_logic(self):
        # update all title sprites
        self.all_sprites.update()
        
    def render(self):
        # fill screen with title background color
        self.title_screen.fill(self.bg_color)
        # drawe all title sprites
        self.all_sprites.draw(self.title_screen)
        

##
# Class: Main()
# Generates the start screen and handle it's events
##

class Main(Title):
    
    def __init__(self, eventhandler, settings):
        self.settings = settings
        
        super().__init__(self.settings.get_screen(), eventhandler, self.settings.color('background'))
        
        self.title_text = Textfield(
            self.settings.get_display_resolution(True, False) / 2,
            20,
            'Paladrium',
            (255, 255, 255),
            60,
            'center',
            self.settings)
        
        # insert start game button
        self.start_button = Button(
            self.settings.get_display_resolution(True, False) / 2 - self.settings.get_button_size(True, False) / 2,
            self.settings.get_display_resolution(False, True) / 2 - self.settings.get_button_size(False, True),
            self.settings.get_button_size(True, False), self.settings.get_button_size(False, True),
            self.cb_start_game,
            'New Game',
            (0, 0, 0),
            self.settings)
        
        # insert quit game button
        self.quit_button = Button(
            self.settings.get_display_resolution(True, False) / 2 - self.settings.get_button_size(True, False) / 2,
            self.settings.get_display_resolution(False, True) / 2 + self.settings.get_button_size(False, True),
            self.settings.get_button_size(True, False), self.settings.get_button_size(False, True),
            self.cb_quit_game,
            'Quit Game',
            (0, 0, 0),
            self.settings)
        
        # add buttons to the title sprite group
        self.all_sprites.add(self.title_text, self.start_button, self.quit_button)
        
    # callback function for quit game button
    def cb_quit_game(self):
        pygame.event.post(self.eventhandler.e_quitgame)
    
    # callback function for start game button 
    def cb_start_game(self):
        pygame.event.post(self.eventhandler.e_startgame)

        
##
# Class: NewGame()
# Generates the start screen and handle it's events
##

class NewGame(Title):
    
    def __init__(self, eventhandler, settings):
        self.settings = settings
        
        super().__init__(self.settings.get_screen(), eventhandler, self.settings.color('background'))
        
        self.title_text = Textfield(
            self.settings.get_display_resolution(True, False) / 2,
            20,
            'Paladrium',
            (255, 255, 255),
            60,
            'center',
            self.settings)
        
        # TODO: adding Inputfield for Playername    
        
        # insert start game button
        self.start_button = Button(
            self.settings.get_display_resolution(True, False) / 2 - self.settings.get_button_size(True, False) / 2,
            self.settings.get_display_resolution(False, True) / 2 - self.settings.get_button_size(False, True),
            self.settings.get_button_size(True, False), self.settings.get_button_size(False, True),
            self.cb_start_game,
            'Start Game',
            (255, 255, 255),
            self.settings)
        
        # insert main menu button
        self.mainmenu_button = Button(
            self.settings.get_display_resolution(True, False) / 2 - self.settings.get_button_size(True, False) / 2,
            self.settings.get_display_resolution(False, True) / 2 + self.settings.get_button_size(False, True),
            self.settings.get_button_size(True, False), self.settings.get_button_size(False, True),
            self.cb_main_menu,
            'Main Menu',
            (255, 255, 255),
            self.settings)
        
        # add buttons to the title sprite group
        self.all_sprites.add(self.title_text, self.start_button, self.mainmenu_button)
    
    # callback function for start game button 
    def cb_start_game(self):
        pygame.event.post(self.eventhandler.e_newgame)
        
    # callback function for start game button 
    def cb_main_menu(self):
        pygame.event.post(self.eventhandler.e_mainmenu)


##
# Class: Error()
# Generates the start screen and handle it's events
##

class Error(Title):
    
    def __init__(self, eventhandler, settings):
        self.settings = settings
        
        super().__init__(self.settings.get_screen(), eventhandler, self.settings.color('background'))
        
        self.title_text = Textfield(
            self.settings.get_display_resolution(True, False) / 2,
            20,
            'Paladrium',
            (255, 255, 255),
            60,
            'center',
            self.settings)
        
        self.error_text = Textfield(
            self.settings.get_display_resolution(True, False) / 2,
            100,
            'Hm...something went wrong',
            (255, 0, 0),
            self.settings.get_font_size_std(),
            'center',
            self.settings)
        
        # insert quit game button
        self.quit_button = Button(
            self.settings.get_display_resolution(True, False) / 2 - self.settings.get_button_size(True, False) / 2,
            self.settings.get_display_resolution(False, True) / 2 - self.settings.get_button_size(False, True),
            self.settings.get_button_size(True, False), self.settings.get_button_size(False, True),
            self.cb_quit_game,
            'Quit Game',
            (255, 255, 255),
            self.settings)
        
        # add buttons to the title sprite group
        self.all_sprites.add(self.title_text, self.error_text, self.quit_button)
        
    # callback function for quit game button
    def cb_quit_game(self):
        pygame.event.post(self.eventhandler.e_quitgame)


##
# Class: Textfield()
# Helper class to show, customize and align text on a title
##

class Textfield(pygame.sprite.Sprite):
    
    def __init__(self, x, y, text, text_color, fontsize, position, settings):
        self.settings = settings
        
        super().__init__()
        
        font = pygame.font.SysFont(self.settings.get_font_std(), fontsize)
        
        text_width, text_height = font.size(text)
        
        self.image = pygame.Surface((text_width, text_height))
        self.image.set_colorkey((0, 0, 0))
        
        if position == 'left':
            self.rect = self.image.get_rect(topleft=(x, y))
        elif position == 'center':
            self.rect = self.image.get_rect(topleft=(x - text_width / 2, y))
        elif position == 'right':
            self.rect = self.image.get_rect(topleft=(x * 2 - text_width, y))
        
        text_surf = font.render(text, True, text_color)
        text_rect = text_surf.get_rect()
        
        self.image.blit(text_surf, text_rect)
        
    def handle_event(self, event):
        return


##
# Class: Button()
# Helper class to create buttons and their interactions on a title
# Initial source code by skrx from stackoverflow.com (https://stackoverflow.com/users/6220679/skrx)
##

class Button(pygame.sprite.Sprite):
    
    def __init__(self, x, y, width, height, callback, text, text_color, settings):
        self.settings = settings
        
        super().__init__()
        
        font = pygame.font.SysFont(self.settings.get_font_std(), self.settings.get_font_size_std())
        
        # load button images and convert alpha
        self.image_normal = pygame.image.load(self.settings.get_button_image_file()).convert_alpha()
        self.image_hover = pygame.image.load(self.settings.get_button_hover_image_file()).convert_alpha()
        self.image_down = pygame.image.load(self.settings.get_button_down_image_file()).convert_alpha()
        
        # scale button images to given button size
        self.image_normal = pygame.transform.scale(self.image_normal, (width, height))
        self.image_hover = pygame.transform.scale(self.image_hover, (width, height))
        self.image_down = pygame.transform.scale(self.image_down, (width, height))

        # use 'normal' as current
        self.image = self.image_normal
        self.rect = self.image.get_rect(topleft=(x, y))
        
        # center text rect
        image_center_x, image_center_y = self.image.get_rect().center
        padding = self.settings.get_button_text_padding()
        top_padding = self.settings.get_button_text_padding()[2] - self.settings.get_button_text_padding()[0]
        left_padding = self.settings.get_button_text_padding()[3] - self.settings.get_button_text_padding()[1]
        text_surf = font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=(image_center_x - left_padding, image_center_y - top_padding))
        
        # blit text onto images
        for image in (self.image_normal, self.image_hover, self.image_down):
            image.blit(text_surf, text_rect)

        # callback function will be called when button gets pressed
        self.callback = callback
        self.button_down = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.image = self.image_down
                self.button_down = True
                
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos) and self.button_down:
                self.callback()
                self.image = self.image_hover
            self.button_down = False
            
        elif event.type == pygame.MOUSEMOTION:
            collided = self.rect.collidepoint(event.pos)
            if collided and not self.button_down:
                self.image = self.image_hover
            elif not collided:
                self.image = self.image_normal
                