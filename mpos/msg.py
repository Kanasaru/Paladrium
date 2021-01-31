"""This module contains constants and messages of mpos

:function echo: formats given values

.. note:: exports no objects
.. note:: raises no exceptions

"""
VERSION = "MPoS 1.0.0 beta"
MPOS = "Moin! MPoS here."

E_KEY = "Given key does not exist."
E_KEYTYPE = "Wrong type of given key."
E_FORMAT = "Wrong format of given attributes."
E_MODE = "Unknown mode."
E_FILE = "File not found."
E_TITLE = "Given title does not exist."

def echo(modul, name, message, data=None):
    """Formats given values.
    
    :param name: name of he modul
    :param message: name of function, class or file
    :param message: logging message
    :param data: optional information
    :type name: mixed
    :type name: mixed
    :type message: mixed
    :type data: mixed
    :returns: formatted logging string
    :rtype: str
    
    """
    msg = str(modul) + ":" + str(name) + ":" + str(message)
    if data is not None:
        msg += "::" + str(data)
    
    return msg
