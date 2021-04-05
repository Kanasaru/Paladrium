"""This module contains functions for attribute handling in mpos

:method set_attr: sets one or multiple attributes
:method get_attr: returns one or all attribute(s)

.. note:: exports no objects
.. note:: raises no own exceptions

"""
import mpos.msg
from mpos.helpers.logger import log

MODUL = __name__

def set_attr(attr_target, attr_source):
    """Sets one or multiple attributes.
    
    :param attributes: contains one or more attributes
    :type attributes: dict or tuple
    
    """
    NAME = set_attr.__name__
    
    if isinstance(attr_source, tuple) and len(attr_source) == 2:
        if attr_source[0] in attr_target:
            attr_target[attr_source[0]] = attr_source[1]
        else:
            log.info(mpos.msg.echo(MODUL, NAME, mpos.msg.E_KEY))
            return False
    elif isinstance(attr_source, dict):
        for key, value in attr_source.items():
            if key in attr_target:
                attr_target[key] = value
            else:
                log.info(mpos.msg.echo(MODUL, NAME, mpos.msg.E_KEY))
    else:
        log.info(mpos.msg.echo(MODUL, NAME, mpos.msg.E_FORMAT))
        return False

    return True
        
def get_attr(attr_target, key=None):
    """Returns one or all attribute(s).
        
    :param key: key of attribute in dict
    :type key: str
        
    """
    NAME = get_attr.__name__
    
    if key is not None:
        if isinstance(key, str):
            if key in attr_target:
                return attr_target[key]
            else:
                log.info(mpos.msg.echo(MODUL, NAME, mpos.msg.E_KEY))
                return False 
        else:
            log.info(mpos.msg.echo(MODUL, NAME, mpos.msg.E_KEYTYPE))
            return False
    else:
        return attr_target
