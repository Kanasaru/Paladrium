"""This module contains constants, functions and classes for
mpos.helpers.debug handling

:class Debugger: creates a debug info object

.. note:: exports no objects
.. note:: raises no exceptions

"""
import pygame
import mpos.msg
import mpos.helpers.time
from mpos.helpers.logger import log

MODUL = __name__

QUIET = 0
LOUD = 1

class Debugger():
    """This class provides a debug info object.
    
    :method __init__: sets up the debugger
    :method toggle: toggles the debug mode
    :method set_mode: sets the debug mode
    :method get_mode: get current debug mode
    :method is_mode: checks if debug mode is as assumed
    :method get_str_timer: formats debug timer in counter string
    
    """
    def __init__(self, mode=QUIET):
        """Sets up the debugger.
        
        :param mode: contains debug mode
        :type: int
        
        :Example:
        
        >>> import mpos.helpers.debug
        >>> a = mpos.helpers.debug.Debugger(mpos.helpers.debug.LOUD)
        
        """
        self.NAME = self.__class__.__name__
        
        self.set_mode(mode)
        self.timer = pygame.time.get_ticks()
        
    def toggle(self):
        """Toggles the debug mode.
        
        :Example:
        
        >>> import mpos.helpers.debug
        >>> a = mpos.helpers.debug.Debugger()
        >>> a.toggle()
        
        """
        if self.mode == LOUD:
            self.mode = QUIET
        else:
            self.mode = LOUD
            
    def set_mode(self, mode):
        """Sets the debug mode.
        
        :param mode: debug mode
        :type: int
        
        :Example:
        
        >>> import mpos.helpers.debug
        >>> a = mpos.helpers.debug.Debugger()
        >>> a.set_mode(mpos.helpers.debug.LOUD)
        
        """
        if mode == QUIET:
            self.mode = QUIET
        elif mode == LOUD:
            self.mode = LOUD
        else:
            log.info(mpos.msg.echo(MODUL, self.NAME, mpos.msg.E_MODE))
            self.mode = QUIET
        
    def get_mode(self):
        """Get current debug mode.
        
        :returns: current debug mode
        :rtype: int
        
        :Example:
        
        >>> import mpos.helpers.debug
        >>> a = mpos.helpers.debug.Debugger()
        >>> mode = a.get_mode()
        
        """
        return self.mode
            
    def is_mode(self, mode):
        """Checks if debug mode is as assumed.
        
        :returns: positive if matching
        :rtype: bool
        
        :Example:
        
        >>> import mpos.helpers.debug
        >>> a = mpos.helpers.debug.Debugger()
        >>> b = a.is_mode(mpos.helpers.debug.LOUD)
        
        """
        if mode == self.mode:
            return True
        else:
            return False
            
    def get_str_timer(self):
        """Formats debug timer in counter string.
        
        :returns: formatted debug timer
        :rtype: str
        
        :Example:
        
        >>> import mpos.helpers.debug
        >>> a = mpos.helpers.debug.Debugger()
        >>> b = a.get_str_timer()
        
        """
        time_diff = pygame.time.get_ticks()-self.timer
        seconds = time_diff//1000
        
        return mpos.helpers.time.seconds_to_clock(seconds)
