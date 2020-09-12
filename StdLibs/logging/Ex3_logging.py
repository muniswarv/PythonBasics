#!/usr/bin/env python
"""

"""


import logging
import EX3_Aux_Logging_mod as  Aux


"""
     Creating a Logger
        - Set the level
frmt = '%(levelname)-8s : %(lineno)-6s : %(message)s'
    
      Create a handlers objects
        - set levels
        - set format
        - add to the logger

      imported module has a logger
"""

frmt = '%(levelname)-8s : %(lineno)-6s : %(message)s'

logger  = logging.getLogger('./log/Ex3_Global.log')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler('./logs/Ex3_logging.debug.txt',"w")
fh.setLevel(logging.DEBUG)
# formatter_fh = logging.Formatter('%(levelname)-10s - %(filename)s - %(lineno)-6d - %(message)s')
formatter_fh = logging.Formatter('%(filename)-15s:%(lineno)-06d  - %(funcName)-15s\n   %(levelname)-8s - %(message)s')

fh.setFormatter(formatter_fh)
logger.addHandler(fh)

# Create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
formatter_ch = logging.Formatter('%(levelname)-8s - %(name)s - %(message)s')
ch.setFormatter(formatter_ch)
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

#-----------------------------   
#  Loging With Modules 
#-----------------------------   

logger.info('creating an instance of Aux.Auxiliary')
a = Aux.Auxiliary()
b = Aux.Auxiliary()
logger.info('created an instance of Aux.Auxiliary')
logger.info('calling Aux.Auxiliary.do_something')
a.do_something()
logger.info('finished Aux.Auxiliary.do_something')
logger.info('calling Aux.some_function()')
Aux.some_function()
logger.info('done with Aux.some_function()')


