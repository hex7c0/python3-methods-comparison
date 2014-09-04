#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
https://wiki.python.org/moin/PythonSpeed/PerformanceTips#Loops

It loops over the elements of a sequence, assigning each to the loop variable.
If the body of your loop is simple,
the interpreter overhead of the for loop itself can be a substantial amount of the overhead.

@author hex7c0 <hex7c0@gmail.com>
'''

import timeit
lst = [0, 11, 33, 44, 55, 66, 77, 88, 99, 0, 'foo', 'pippo']

def normal():

    a = []
    for i in lst:
        a.append(str(i))
    return a

def nodots():

    a = []
    fx = a.append
    for i in lst:
        fx(str(i))
    return a

def nodots_local():

    local_lst = [0, 11, 33, 44, 55, 66, 77, 88, 99, 0, 'foo', 'pippo']
    a = []
    fx = a.append
    for i in local_lst:
        fx(str(i))
    return a

def mapp():
    # map on python > 3
    # return a iterator and not a list

    b = list(map(str, lst))
    return b

def union():

    a = []
    local_lst = [0, 11, 33, 44, 55, 66, 77, 88, 99, 0, 'foo', 'pippo']
    fx = a.append
    for i in map(str, local_lst):
        fx(i)
    return a


if __name__ == '__main__':

    jointimer = timeit.Timer('normal()', 'from __main__ import normal')
    print ('Normal method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('nodots()', 'from __main__ import nodots')
    print ('Nodots method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('nodots_local()', 'from __main__ import nodots_local')
    print ('NodotsLocal method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('mapp()', 'from __main__ import mapp')
    print ('Mapp method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('union()', 'from __main__ import union')
    print ('Union method took %f seconds' % jointimer.timeit())

    # test
    if(normal() == nodots() == nodots_local() == union()):
        quit()
    quit('Fail')
