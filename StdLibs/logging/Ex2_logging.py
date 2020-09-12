#!/usr/bin/env python

import logging

# logging.basicConfig(format='%(levelname)s:%0(lineno)6s:%(message)s', level=logging.DEBUG)

#logfile  = './logs/EX1_BasicLogging_Ver1.log'   ; # File name  


filemode = "w"  # w a
frmt     = '%(levelname)-8s : %(lineno)-6s : %(message)s',

# Default :   StdError
logging.basicConfig( format=frmt,
                     level=logging.DEBUG)

                     # filename="./log/Ex2_logging.log",

logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')
