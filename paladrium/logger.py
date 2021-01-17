import logging
import mpos.helpers.logger

log = logging.getLogger('paladrium')
log.setLevel(logging.DEBUG)

if (log.hasHandlers()):
    log.handlers.clear()

fh = logging.FileHandler('paladrium.log')
fh.setLevel(logging.DEBUG)

log.addHandler(fh)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

log.addHandler(fh)
