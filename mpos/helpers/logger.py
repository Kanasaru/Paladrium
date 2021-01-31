"""This module contains everything about logging of mpos package

.. note:: provides object log
.. note:: raises no exceptions

"""
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('mpos')