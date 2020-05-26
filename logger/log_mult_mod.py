#%% 
import logging
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
#%%
import mylib

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    
    for i in range(10):
        mylib.do_something()
    
    logging.info('Finished')

if __name__ == '__main__':
    main()