#########################################
# Paladrium - a RPG Project             #
# https://github.com/Kanasaru/Paladrium #
# GPL 3.0 License                       #
#########################################


### IMPORTS & INITIALISATON

# PyGame
import pygame

# Paladrium packages
from . import constants
from . import events


### CONSTANTS

IMAGE_NORMAL = pygame.Surface((100, 32))
IMAGE_NORMAL.fill(pygame.Color('dodgerblue1'))
IMAGE_HOVER = pygame.Surface((100, 32))
IMAGE_HOVER.fill(pygame.Color('lightskyblue'))
IMAGE_DOWN = pygame.Surface((100, 32))
IMAGE_DOWN.fill(pygame.Color('aquamarine1'))
FONT = pygame.font.SysFont('Comic Sans MS', 16)

STD_BUTTON_WIDTH  = 160
STD_BUTTON_HEIGHT = 40


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
    
    def __init__(self, screen, eventhandler):
        super().__init__(screen, eventhandler, constants.BLACK)
        
        self.title_text = Textfield(
            constants.DISPLAYWIDTH / 2,
            20,
            'Paladrium',
            (255, 255, 255),
            'center',
            pygame.font.SysFont('Comic Sans MS', 60))
        
        # insert start game button
        self.start_button = Button(
            constants.DISPLAYWIDTH / 2 - STD_BUTTON_WIDTH / 2,
            constants.DISPLAYHEIGHT / 2 - STD_BUTTON_HEIGHT,
            STD_BUTTON_WIDTH, STD_BUTTON_HEIGHT,
            self.cb_start_game,
            FONT,
            'New Game',
            (255, 255, 255))
        
        # insert quit game button
        self.quit_button = Button(
            constants.DISPLAYWIDTH / 2 - STD_BUTTON_WIDTH / 2,
            constants.DISPLAYHEIGHT / 2 + STD_BUTTON_HEIGHT,
            STD_BUTTON_WIDTH, STD_BUTTON_HEIGHT,
            self.cb_quit_game,
            FONT,
            'Quit Game',
            (255, 255, 255))
        
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
    
    def __init__(self, screen, eventhandler):
        super().__init__(screen, eventhandler, constants.BLACK)
        
        self.title_text = Textfield(
            constants.DISPLAYWIDTH / 2,
            20,
            'Paladrium',
            (255, 255, 255),
            'center',
            pygame.font.SysFont('Comic Sans MS', 60))
        
        # TODO: adding Inputfield for Playername    
        
        # insert start game button
        self.start_button = Button(
            constants.DISPLAYWIDTH / 2 - STD_BUTTON_WIDTH / 2,
            constants.DISPLAYHEIGHT / 2 - STD_BUTTON_HEIGHT,
            STD_BUTTON_WIDTH, STD_BUTTON_HEIGHT,
            self.cb_start_game,
            FONT,
            'Start Game',
            (255, 255, 255))
        
        # insert main menu button
        self.mainmenu_button = Button(
            constants.DISPLAYWIDTH / 2 - STD_BUTTON_WIDTH / 2,
            constants.DISPLAYHEIGHT / 2 + STD_BUTTON_HEIGHT,
            STD_BUTTON_WIDTH, STD_BUTTON_HEIGHT,
            self.cb_main_menu,
            FONT,
            'Main Menu',
            (255, 255, 255))
        
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
    
    def __init__(self, screen, eventhandler):
        super().__init__(screen, eventhandler, constants.BLACK)
        
        self.title_text = Textfield(
            constants.DISPLAYWIDTH / 2,
            20,
            'Paladrium',
            (255, 255, 255),
            'center',
            pygame.font.SysFont('Comic Sans MS', 60))
        
        self.error_text = Textfield(
            constants.DISPLAYWIDTH / 2,
            100,
            'Hm...something went wrong',
            (255, 0, 0),
            'center',
            pygame.font.SysFont('Comic Sans MS', 24))
        
        # insert quit game button
        self.quit_button = Button(
            constants.DISPLAYWIDTH / 2 - STD_BUTTON_WIDTH / 2,
            constants.DISPLAYHEIGHT / 2,
            STD_BUTTON_WIDTH, STD_BUTTON_HEIGHT,
            self.cb_quit_game,
            FONT,
            'Quit Game',
            (255, 255, 255))
        
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
    
    def __init__(self, x, y, text='', text_color=(0, 0, 0), position='left', font=FONT):
        super().__init__()
        
        text_width, text_height = font.size(text)
        
        self.image = pygame.Surface((text_width, text_height))
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

    def __init__(self, x, y, width, height, callback,
                 font=FONT, text='', text_color=(0, 0, 0),
                 image_normal=IMAGE_NORMAL, image_hover=IMAGE_HOVER,
                 image_down=IMAGE_DOWN):
        super().__init__()
        
        # scale button images to given button size
        self.image_normal = pygame.transform.scale(image_normal, (width, height))
        self.image_hover = pygame.transform.scale(image_hover, (width, height))
        self.image_down = pygame.transform.scale(image_down, (width, height))

        # use 'normal' as current
        self.image = self.image_normal
        self.rect = self.image.get_rect(topleft=(x, y))
        
        # center text rect
        image_center = self.image.get_rect().center
        text_surf = font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=image_center)
        
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
                