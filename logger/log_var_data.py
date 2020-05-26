#%% 
import logging
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
#%%
import random

#%%
def main():
    logging.basicConfig(filename='myfloat.log', level=logging.INFO)
    logging.info('Started')
    
    for i in range(10):
        x=random.uniform(0,10)
        logging.info('My random float: %.2f' % x)
    
    logging.info('Finished')

if __name__ == '__main__':
    main()