#%% 
import logging
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

def do_something():
    logging.info('Doing something')
