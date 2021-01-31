"""This module contains constants, functions and classes for
mpos.helpers.time handling

:method seconds_to_clock: transforms int to timestring

.. note:: exports no objects
.. note:: raises no own exceptions

"""
import mpos.msg
from mpos.helpers.logger import log

MODUL = __name__

def seconds_to_clock(seconds):
    """Transforms int to timestring.
        
    :param attributes: seconds to transform
    :type: int
    :returns: clock format like '00:00:00'
    :type: str
    
    :Example:
    
    >>> import mpos.helpers
    >>> a = 123456789
    >>> b = mpos.helpers.time.seconds_to_clock(a)
    
    """
    timestring = ""
    
    if seconds < 0:
        seconds = seconds * (-1)
        negative = True
    else:
        negative = False
        
    hours = seconds // 3600
    minutes = (seconds - (hours * 3600)) // 60
    seconds -= (seconds - (hours * 3600)) - (seconds - (minutes * 60))
        
    if hours < 10:
        hours = "0" + str(hours)
    else:
        hours = str(hours)
    if minutes < 10:
        minutes = "0" + str(minutes)
    else:
        minutes = str(minutes)
    if seconds < 10:
        seconds = "0" + str(seconds)
    else:
        seconds = str(seconds)
        
    if negative:
        timestring += "-"
        
    timestring += str(hours) + ":" + str(minutes) + ":" + str(seconds)
    
    return timestring
