#!/usr/bin/env python

""" Example 1 for learning logging module

    Send all the log messages to a specified logfile
        - Defualt form message
        - User defined format
        - Log mode : append or write mode
        - setting the levels

    Set the file name directly to default log handler

    Need to know   
"""

import sys
import logging


def main():

    """
        XYz
    """

    #log = logging.logger();
    #logging.shutdown()

    logfile  = './logs/EX1_BasicLogging_Ver1.log'   ; # File name  
    filemode = "w"  # w a
    frmt     = '%(levelname)-8s : %(lineno)-6s : %(message)s',
    logging.basicConfig(filename=logfile,
                        filemode=filemode,
                        level=logging.DEBUG)

                        #format=frmt,
    print "Creating Logging file" , logfile

    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')

    #logging.shutdown()

main()
