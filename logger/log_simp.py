
#%% simple
import logging
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

for i in range(10):
    logging.warning('Watch out!')
    logging.info('I told you so.') #does not print
    
#%% to_file
import logging

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
    
logging.basicConfig(filename='./example.log',level=logging.DEBUG)

for i in range(10):
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')