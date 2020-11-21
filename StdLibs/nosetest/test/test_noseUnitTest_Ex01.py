#!/usr/bin/env python


#from unnecessary_math import multiply


def multiply(a,b):     return a*b
def test_numbers_3_4():
    assert multiply(3,4) == 12 

def test_strings_a_3():
    assert multiply('a',3) == 'aaa' 

def my_setup_function():
    print "Running my_setup_function"
    pass

def my_teardown_function():
    print "Running my_teardown_function"
    pass


#@with_setup(my_setup_function, my_teardown_function)
def test_numbers_3_4_setup():
    print "Running test_numbers_3_4"
    assert multiply(3,4) == 12 
