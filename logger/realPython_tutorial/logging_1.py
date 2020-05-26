def main(): 
    logging.debug('this is a debug message.')
    logging.info('this is an info message.')
    logging.warning('this is a warning message.')
    logging.error('this is an error message.')
    logging.critical('this is a critical message.')

def main6():
    error_var='Voldemort'
    logging.error('this is an error message raised by %s.',error_var)
    logging.error(f'this is another error message raised by {error_var}')

def main7():
    a=5
    b=0

    try:
        c=a/b
    except Exception as e:
        # important: set exc_info to True to provide detailed error info
        # method 1:
        # logging.error('Exception occurred, method 1.',exc_info=True)
        # method 2:
        logging.exception("Exception occurred, method 2.")



if __name__=="__main__":
    import logging
    #%% EX1: DEFAULT
    # many different types of logging messages.  Assigns root to default logger. 
    # Format: level:name:message 
    # default, only warning or above is logged.  debug and info ignored.
    # main()

    #%% EX 2: CHANGE LEVEL OF LOGS
    # print('[INFO] Change level of messages to log.\r\n')
    # logging.basicConfig(level=logging.DEBUG)
    # # all levels will be reported
    # main()

    #%% EX3: CHANGE ALL SETTINGS
    # logging.basicConfig(level=logging.DEBUG, filename='ex3.log', format='%(name)s - %(levelname)s - %(message)s')
    # main()

    #%% EX4: Log process ID
    # logging.basicConfig(level=logging.DEBUG, filename='ex4.log', format='%(name)s - %(process)d - %(levelname)s - %(message)s')
    # main()

    #%% EX5: Add date and time
    # logging.basicConfig(level=logging.DEBUG, filename='ex5.log', format='%(asctime)s - %(name)s - %(process)d - %(levelname)s - %(message)s')
    # main()

    #%% EX6: pass variable
    # logging.basicConfig(level=logging.DEBUG, filename='ex6.log', format='%(asctime)s - %(name)s - %(process)d - %(levelname)s - %(message)s')
    # main6()

    #%% EX7: stacktraces
    logging.basicConfig(filename='ex7.log', format='%(asctime)s - %(name)s - %(process)d - %(levelname)s - %(message)s')
    main7()



