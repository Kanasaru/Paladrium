#########################################
# Paladrium - a RPG Project             #
# https://github.com/Kanasaru/Paladrium #
# GPL 3.0 License                       #
#########################################

### IMPORTS & INITIALISATON

import mpos.helpers.event
import mpos.forms

import paladrium.events
from paladrium.logger import log
from paladrium.settings import settings

### CONSTANTS

# Paladrium titles
MAIN       = 1000
NEWGAME    = 1001
OPTIONS    = 1002
RESOLUTION = 1003
SOUNDS     = 1004
CONTROLS   = 1005


### CLASSES & FUNCTIONS

def build_title(identifier):
    
    # create a title
    attr = {
        "pos_x":            0,
        "pos_y":            0,
        "width":            settings.get_display_resolution(True, False),
        "height":           settings.get_display_resolution(False, True),
        "text":             "",
        "text_font":        "assets/fonts/Cinzel-Medium.ttf",
        "font_size":        20,
        "font_color":       (0, 0 ,0),
        "background_color": settings.color('background'),
        "colorkey":         None,
        "transparency":     255
    }
    title = mpos.forms.title.Title(attr)
    
    # build up Paladrium headline
    attr = {
        "pos-y":        20,
        "text":         "Paladrium",
        "text-size":    60,
    }
    tf_headline = mpos.forms.textbox.Textbox(attr)
    tf_headline.set_attr(("pos-x", settings.get_display_resolution(True, False) / 2 - tf_headline.width() / 2))
    
    # add headline to title
    title.add(tf_headline)
    
    # stay away, next forms object
    width, height = tf_headline.get_dimensions()
    position_y = height + 100
    
    # which title has to be build?
    if identifier == paladrium.titles.MAIN:
        
        # build up button
        attr = {
            "pos-y":            position_y,
            "text":             "New Game",
            "callback_event":   mpos.helpers.event.Event(paladrium.events.NEWTITLE, NEWGAME)
        }
        b_newgame = mpos.forms.button.Button(attr)
        
        # apply padding
        pos_x = settings.get_display_resolution(True, False) / 2 - b_newgame.get_attr("width") / 2
        b_newgame.set_attr(("pos-x", pos_x))
        
        # stay away, next forms object
        width, height = b_newgame.get_dimensions()
        position_y += height + 20
        
        # build up button
        attr = {
            "pos-y":          position_y,
            "text":           "Load Game",
            "callback_event": mpos.helpers.event.Event(paladrium.events.LOADGAME, ""),
            "clickable":      False
        }
        b_loadgame = mpos.forms.button.Button(attr)
        
        # apply padding
        pos_x = settings.get_display_resolution(True, False) / 2 - b_loadgame.get_attr("width") / 2
        b_loadgame.set_attr(("pos-x", pos_x))
        
        # stay away, next forms object
        width, height = b_loadgame.get_dimensions()
        position_y += height + 20
        
        # build up button
        attr = {
            "pos-y":          position_y,
            "text":           "Options",
            "callback_event": mpos.helpers.event.Event(paladrium.events.NEWTITLE, OPTIONS)
        }
        b_options = mpos.forms.button.Button(attr)
        
        # apply padding
        pos_x = settings.get_display_resolution(True, False) / 2 - b_options.get_attr("width") / 2
        b_options.set_attr(("pos-x", pos_x))
        
        # stay away, next forms object
        width, height = b_options.get_dimensions()
        position_y += height + 20
        
        # build up button
        attr = {
            "pos-y":          position_y,
            "text":           "Quit Game",
            "callback_event": mpos.helpers.event.Event(paladrium.events.QUITGAME, "")
        }
        b_quitgame = mpos.forms.button.Button(attr)
        
        # apply padding
        pos_x = settings.get_display_resolution(True, False) / 2 - b_quitgame.get_attr("width") / 2
        b_quitgame.set_attr(("pos-x", pos_x))
        
        # add forms objects to title
        title.add(b_newgame)
        title.add(b_loadgame)
        title.add(b_options)
        title.add(b_quitgame)
        
    elif identifier == paladrium.titles.NEWGAME:
        
        # build up button
        attr = {
            "pos-y":            position_y,
            "text":             "Start Game",
            "callback_event":   mpos.helpers.event.Event(paladrium.events.STARTGAME, "")
        }
        b_startgame = mpos.forms.button.Button(attr)
        
        # apply padding
        pos_x = settings.get_display_resolution(True, False) / 2 - b_startgame.get_attr("width") / 2
        b_startgame.set_attr(("pos-x", pos_x))
        
        # stay away, next forms object
        width, height = b_startgame.get_dimensions()
        position_y += height + 20
        
        # build up button
        attr = {
            "pos-y":          position_y,
            "text":           "Back",
            "callback_event": mpos.helpers.event.Event(paladrium.events.NEWTITLE, MAIN)
        }
        b_back = mpos.forms.button.Button(attr)
        
        # apply padding
        pos_x = settings.get_display_resolution(True, False) / 2 - b_back.get_attr("width") / 2
        b_back.set_attr(("pos-x", pos_x))
        
        # add forms objects to title
        title.add(b_startgame)
        title.add(b_back)
        
    elif identifier == paladrium.titles.OPTIONS:
        
        # build up button
        attr = {
            "pos-y":            position_y,
            "text":             "Resolutions",
            "callback_event":   mpos.helpers.event.Event(paladrium.events.NEWTITLE, RESOLUTION)
        }
        b_resolution = mpos.forms.button.Button(attr)
        
        # apply padding
        pos_x = settings.get_display_resolution(True, False) / 2 - b_resolution.get_attr("width") / 2
        b_resolution.set_attr(("pos-x", pos_x))
        
        # stay away, next forms object
        width, height = b_resolution.get_dimensions()
        position_y += height + 20
        
        # build up button
        attr = {
            "pos-y":          position_y,
            "text":           "Sounds",
            "callback_event": mpos.helpers.event.Event(paladrium.events.NEWTITLE, SOUNDS),
            "clickable":      False
        }
        b_sounds = mpos.forms.button.Button(attr)
        
        # apply padding
        pos_x = settings.get_display_resolution(True, False) / 2 - b_sounds.get_attr("width") / 2
        b_sounds.set_attr(("pos-x", pos_x))
        
        # stay away, next forms object
        width, height = b_sounds.get_dimensions()
        position_y += height + 20
        
        # build up button
        attr = {
            "pos-y":          position_y,
            "text":           "Controls",
            "callback_event": mpos.helpers.event.Event(paladrium.events.NEWTITLE, CONTROLS),
            "clickable":      False
        }
        b_controls = mpos.forms.button.Button(attr)
        
        # apply padding
        pos_x = settings.get_display_resolution(True, False) / 2 - b_controls.get_attr("width") / 2
        b_controls.set_attr(("pos-x", pos_x))
        
        # stay away, next forms object
        width, height = b_controls.get_dimensions()
        position_y += height + 20
        
        # build up button
        attr = {
            "pos-y":          position_y,
            "text":           "Back",
            "callback_event": mpos.helpers.event.Event(paladrium.events.NEWTITLE, MAIN)
        }
        b_back = mpos.forms.button.Button(attr)
        
        # apply padding
        pos_x = settings.get_display_resolution(True, False) / 2 - b_back.get_attr("width") / 2
        b_back.set_attr(("pos-x", pos_x))
        
        # add forms objects to title
        title.add(b_resolution)
        title.add(b_sounds)
        title.add(b_controls)
        title.add(b_back)
        
    elif identifier == paladrium.titles.RESOLUTION:
        
        # build up button
        if settings.is_resolution((640, 480)):
            clickable = False
        else:
            clickable = True
        
        attr = {
            "pos-y":            position_y,
            "text":             "640 x 480",
            "callback_event":   mpos.helpers.event.Event(paladrium.events.RESOLUTION, (640, 480)),
            "clickable":        clickable
        }
        b_resolution_640 = mpos.forms.button.Button(attr)
        
        # apply padding
        pos_x = settings.get_display_resolution(True, False) / 2 - b_resolution_640.get_attr("width") / 2
        b_resolution_640.set_attr(("pos-x", pos_x))
        
        # stay away, next forms object
        width, height = b_resolution_640.get_dimensions()
        position_y += height + 20
        
        # build up button
        if settings.is_resolution((1280, 720)):
            clickable = False
        else:
            clickable = True
        
        attr = {
            "pos-y":            position_y,
            "text":             "1280 x 720",
            "callback_event":   mpos.helpers.event.Event(paladrium.events.RESOLUTION, (1280, 720)),
            "clickable":        clickable
        }
        b_resolution_1280 = mpos.forms.button.Button(attr)
        
        # apply padding
        pos_x = settings.get_display_resolution(True, False) / 2 - b_resolution_1280.get_attr("width") / 2
        b_resolution_1280.set_attr(("pos-x", pos_x))
        
        # stay away, next forms object
        width, height = b_resolution_1280.get_dimensions()
        position_y += height + 20
        
        # build up button
        attr = {
            "pos-y":          position_y,
            "text":           "Back",
            "callback_event": mpos.helpers.event.Event(paladrium.events.NEWTITLE, OPTIONS)
        }
        b_back = mpos.forms.button.Button(attr)
        
        # apply padding
        pos_x = settings.get_display_resolution(True, False) / 2 - b_back.get_attr("width") / 2
        b_back.set_attr(("pos-x", pos_x))
        
        # add forms objects to title
        title.add(b_resolution_640)
        title.add(b_resolution_1280)
        title.add(b_back)
        
    else:
        log.info("Game().build_title(): Given title does not exist")
        
    return title