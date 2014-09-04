#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Best method for switch in Python
because isn't not built-in

@author hex7c0 <hex7c0@gmail.com>
'''

import timeit

def classic(n):
    if(n == 0):
        n = 0
    elif(n == 1):
        n = 1
    elif(n == 2):
        n = 2
    elif(n == 3):
        n = 3
    else:
        n = 0
    return n

def dictionary(n):

    try:
        return {
            0:0,
            1:1,
            2:2,
            3:3
            }[n]
    except KeyError:  # else
        return 0

switch = {
            0:0,
            1:1,
            2:2,
            3:3
            }
def closure(n):

    try:
        return switch[n]
    except KeyError:  # else
        return 0

def closure_no_try(n):

    if(n >= 0 and n <= 3):
        return switch[n]
    else:
        return 0

if __name__ == '__main__':

    jointimer = timeit.Timer('classic(1)', 'from __main__ import classic')
    print ('classic get method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('classic(999)', 'from __main__ import classic')
    print ('classic else method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('dictionary(1)', 'from __main__ import dictionary')
    print ('dictionary get method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('dictionary(999)', 'from __main__ import dictionary')
    print ('dictionary else method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('closure(1)', 'from __main__ import closure')
    print ('closure get method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('closure(999)', 'from __main__ import closure')
    print ('closure else method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('closure_no_try(1)', 'from __main__ import closure_no_try')
    print ('closure_no_try get method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('closure_no_try(999)', 'from __main__ import closure_no_try')
    print ('closure_no_try else method took %f seconds' % jointimer.timeit())

    # test
    if(classic(1) == dictionary(1) == closure(1) == closure_no_try(1)):
        if(classic(999) == dictionary(999) == closure(999) == closure_no_try(999)):
            quit()
    quit('Fail')
