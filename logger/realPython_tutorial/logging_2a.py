import logging

logging.basicConfig(level=logging.DEBUG)

# will log as logging_2a whenever logging 2a is imported and do_something is called
log=logging.getLogger(__name__)

def do_something():
    log.debug("doing something")

