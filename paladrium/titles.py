"""This module defines paladrium titles

:function build_title: creates title by id

.. note:: https://github.com/Kanasaru/Paladrium
.. note:: raises no exceptions

"""
import mpos.msg
import mpos.helpers.event
import mpos.forms
import paladrium.events
from paladrium.logger import log
from paladrium.settings import settings

MODUL = __name__

MAIN       = 1000
NEWGAME    = 1001
OPTIONS    = 1002
RESOLUTION = 1003
SOUNDS     = 1004
CONTROLS   = 1005

def build_title(identifier):
    """Creates title by id.
    
    :param identifier: title id
    :type identifier: int
    :returns: created title object
    :rtype: mpos.forms.title.Title
    
    """
    NAME = build_title.__name__
    
    spritesheet = "assets/sprites/buttons.png"
    colorkey = (1, 0, 0)
    display_width = settings.get_display_resolution(True, False)
    
    attr = {
        "pos_x": 0,
        "pos_y": 0,
        "width": settings.get_display_resolution(True, False),
        "height": settings.get_display_resolution(False, True),
        "bg_color": settings.color('background')
    }
    title = mpos.forms.title.Title(attr)
    
    attr = {
        "pos_y": 20,
        "text": "Paladrium",
        "font_size": 60,
        "text_font": "assets/fonts/Cinzel-Medium.ttf"
    }
    tf_headline = mpos.forms.textbox.Textbox(attr)
    pos_x = display_width / 2 - tf_headline.width() / 2
    tf_headline.set_attr(("pos_x", pos_x))
    
    title.add(tf_headline)
    
    width, height = tf_headline.get_dimensions()
    position_y = height + 100
    
    if identifier == paladrium.titles.MAIN:
        attr = {
            "pos_y": position_y,
            "text": "New Game",
            "callback_event": mpos.helpers.event.Event(
                paladrium.events.NEWTITLE,
                NEWGAME
            ),
            "colorkey": colorkey,
            "spritesheet": spritesheet
        }
        b_newgame = mpos.forms.button.Button(attr)
        pos_x = display_width / 2 - b_newgame.get_attr("width") / 2
        b_newgame.set_attr(("pos_x", pos_x))
        
        width, height = b_newgame.get_dimensions()
        position_y += height + 20
        
        attr = {
            "pos_y": position_y,
            "text": "Load Game",
            "callback_event": mpos.helpers.event.Event(
                paladrium.events.LOADGAME,
                ""
            ),
            "clickable": False,
            "colorkey": colorkey,
            "spritesheet": spritesheet
        }
        b_loadgame = mpos.forms.button.Button(attr)
        pos_x = display_width / 2 - b_loadgame.get_attr("width") / 2
        b_loadgame.set_attr(("pos_x", pos_x))
        
        width, height = b_loadgame.get_dimensions()
        position_y += height + 20
        
        attr = {
            "pos_y": position_y,
            "text": "Options",
            "callback_event": mpos.helpers.event.Event(
                paladrium.events.NEWTITLE,
                OPTIONS
            ),
            "colorkey": colorkey,
            "spritesheet": spritesheet
        }
        b_options = mpos.forms.button.Button(attr)
        pos_x = display_width / 2 - b_options.get_attr("width") / 2
        b_options.set_attr(("pos_x", pos_x))
        
        width, height = b_options.get_dimensions()
        position_y += height + 20
        
        attr = {
            "pos_y": position_y,
            "text": "Quit Game",
            "callback_event": mpos.helpers.event.Event(
                paladrium.events.QUITGAME,
                ""
            ),
            "colorkey": colorkey,
            "spritesheet": spritesheet
        }
        b_quitgame = mpos.forms.button.Button(attr)
        pos_x = display_width / 2 - b_quitgame.get_attr("width") / 2
        b_quitgame.set_attr(("pos_x", pos_x))
        
        title.add(b_newgame)
        title.add(b_loadgame)
        title.add(b_options)
        title.add(b_quitgame)
        
    elif identifier == paladrium.titles.NEWGAME:
        
        attr = {
            "pos_y": position_y,
            "text": "Start Game",
            "callback_event":   mpos.helpers.event.Event(
                paladrium.events.STARTGAME,
                ""
            ),
            "colorkey": colorkey,
            "spritesheet": spritesheet
        }
        b_startgame = mpos.forms.button.Button(attr)
        pos_x = display_width / 2 - b_startgame.get_attr("width") / 2
        b_startgame.set_attr(("pos_x", pos_x))
        
        width, height = b_startgame.get_dimensions()
        position_y += height + 20
        
        attr = {
            "pos_y": position_y,
            "text": "Back",
            "callback_event": mpos.helpers.event.Event(
                paladrium.events.NEWTITLE,
                MAIN
            ),
            "colorkey": colorkey,
            "spritesheet": spritesheet
        }
        b_back = mpos.forms.button.Button(attr)
        pos_x = display_width / 2 - b_back.get_attr("width") / 2
        b_back.set_attr(("pos_x", pos_x))
        
        title.add(b_startgame)
        title.add(b_back)
        
    elif identifier == paladrium.titles.OPTIONS:
        
        attr = {
            "pos_y": position_y,
            "text": "Resolutions",
            "callback_event": mpos.helpers.event.Event(
                paladrium.events.NEWTITLE,
                RESOLUTION
            ),
            "colorkey": colorkey,
            "spritesheet": spritesheet
        }
        b_resolution = mpos.forms.button.Button(attr)
        pos_x = display_width / 2 - b_resolution.get_attr("width") / 2
        b_resolution.set_attr(("pos_x", pos_x))
        
        width, height = b_resolution.get_dimensions()
        position_y += height + 20
        
        attr = {
            "pos_y": position_y,
            "text": "Sounds",
            "callback_event": mpos.helpers.event.Event(
                paladrium.events.NEWTITLE,
                SOUNDS
            ),
            "clickable": False,
            "colorkey": colorkey,
            "spritesheet": spritesheet
        }
        b_sounds = mpos.forms.button.Button(attr)
        pos_x = display_width / 2 - b_sounds.get_attr("width") / 2
        b_sounds.set_attr(("pos_x", pos_x))
        
        width, height = b_sounds.get_dimensions()
        position_y += height + 20
        
        attr = {
            "pos_y": position_y,
            "text": "Controls",
            "callback_event": mpos.helpers.event.Event(
                paladrium.events.NEWTITLE,
                CONTROLS
            ),
            "clickable": False,
            "colorkey": colorkey,
            "spritesheet": spritesheet
        }
        b_controls = mpos.forms.button.Button(attr)
        pos_x = display_width / 2 - b_controls.get_attr("width") / 2
        b_controls.set_attr(("pos_x", pos_x))
        
        width, height = b_controls.get_dimensions()
        position_y += height + 20
        
        attr = {
            "pos_y": position_y,
            "text": "Back",
            "callback_event": mpos.helpers.event.Event(
                paladrium.events.NEWTITLE,
                MAIN
            ),
            "colorkey": colorkey,
            "spritesheet": spritesheet
        }
        b_back = mpos.forms.button.Button(attr)
        pos_x = display_width / 2 - b_back.get_attr("width") / 2
        b_back.set_attr(("pos_x", pos_x))
        
        title.add(b_resolution)
        title.add(b_sounds)
        title.add(b_controls)
        title.add(b_back)
        
    elif identifier == paladrium.titles.RESOLUTION:
        
        if settings.is_resolution((640, 480)):
            clickable = False
        else:
            clickable = True
        
        attr = {
            "pos_y": position_y,
            "text": "640 x 480",
            "callback_event": mpos.helpers.event.Event(
                paladrium.events.RESOLUTION,
                (640, 480)
            ),
            "clickable": clickable,
            "colorkey": colorkey,
            "spritesheet": spritesheet
        }
        b_resolution_640 = mpos.forms.button.Button(attr)
        pos_x = display_width / 2 - b_resolution_640.get_attr("width") / 2
        b_resolution_640.set_attr(("pos_x", pos_x))
        
        width, height = b_resolution_640.get_dimensions()
        position_y += height + 20
        
        if settings.is_resolution((1280, 720)):
            clickable = False
        else:
            clickable = True
        
        attr = {
            "pos_y": position_y,
            "text": "1280 x 720",
            "callback_event": mpos.helpers.event.Event(
                paladrium.events.RESOLUTION,
                (1280, 720)
            ),
            "clickable": clickable,
            "colorkey": colorkey,
            "spritesheet": spritesheet
        }
        b_resolution_1280 = mpos.forms.button.Button(attr)
        
        pos_x = display_width / 2 - b_resolution_1280.get_attr("width") / 2
        b_resolution_1280.set_attr(("pos_x", pos_x))
        
        width, height = b_resolution_1280.get_dimensions()
        position_y += height + 20
        
        attr = {
            "pos_y": position_y,
            "text": "Back",
            "callback_event": mpos.helpers.event.Event(
                paladrium.events.NEWTITLE,
                OPTIONS
            ),
            "colorkey": colorkey,
            "spritesheet": spritesheet
        }
        b_back = mpos.forms.button.Button(attr)
        
        pos_x = display_width / 2 - b_back.get_attr("width") / 2
        b_back.set_attr(("pos_x", pos_x))
        
        title.add(b_resolution_640)
        title.add(b_resolution_1280)
        title.add(b_back)
        
    else:
        log.info(mpos.msg.echo(MODUL, NAME, mpos.msg.E_TITLE))
        
    return title
