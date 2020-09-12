#!/usr/bin/env python

import logging

# create logger
module_logger = logging.getLogger('spam_application.auxiliary')

class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger('spam_application.auxiliary.Auxiliary')
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler('./logs/Ex3_Aux_logging.debug.txt',"a")
        #fh = logging.StreamHandler()
        frmt_fh = logging.Formatter('%(levelname)-8s - %(name)s - %(message)s')
        fh.setFormatter(frmt_fh)
        self.logger.addHandler(fh)

        self.logger.info('Aux  :  creating an instance of Auxiliary')
        print 'Aux  :  creating an instance of Auxiliary'

    def do_something(self):
        self.logger.info('Aux  :  doing something')
        a = 1 + 1
        self.logger.info('Aux  :  done doing something')

def some_function():
    module_logger.info('received a call to "some_function"')
