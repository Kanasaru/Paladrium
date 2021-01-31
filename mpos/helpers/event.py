"""This module contains constants, functions and classes for
event handling

:class Event: provides an event object for mpos

.. note:: exports no objects
.. note:: raises no exceptions
.. todo:: 

"""
import mpos.msg
from mpos.helpers.logger import log

MODUL = __name__

class Event():
    """This class provides an event object for mpos.
    
    :method __init__: sets up the event
    :method __str__: controls how an instance will be 'printed'
    
    """
    
    def __init__(self, code, data):
        """Sets up the event.
        
        :param code: identifier of the event
        :param data: contains all event information
        :type code: int
        :type data: mixed
        
        :Example:
        
        >>> import mpos.helpers
        >>> data = {}
        >>> a = mpos.helpers.event.Event(1000, data)
        
        """
        self.NAME = self.__class__.__name__
        
        self.code = code
        self.data = data
        
    def __str__(self):
        """Controls how an instance will be 'printed'.
        
        :returns: formatted output string
        :type: str
        
        :Example:
        
        >>> import mpos.helpers
        >>> data = {}
        >>> a = mpos.helpers.event.Event(1000, data)
        >>> print(a)
        
        """
        printstring = "Event [" + str(self.code) + "]"
        printstring += str(self.data)
        
        return printstring
