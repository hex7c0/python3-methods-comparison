#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Created on 07/gen/2014

https://wiki.python.org/moin/PythonSpeed/PerformanceTips#Data_Aggregation

Function call overhead in Python is relatively high,
especially compared with the execution speed of a builtin function

@author hex7c0 <hex7c0@gmail.com>
'''

import timeit

def outside():

    def a(i):
        x = 1 + i
        return x

    lst = range(10)
    for i in lst:
        o = a(i)
    return o


def inside():

    def a(lst):
        for i in lst:
            x = 1 + i
        return x

    lst = range(10)
    o = a(lst)
    return o

if __name__ == '__main__':

    jointimer = timeit.Timer('outside()', 'from __main__ import outside')
    print('Outside method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('inside()', 'from __main__ import inside')
    print('Inside method took %f seconds' % jointimer.timeit())

    # test
    if(inside() == outside()):
        quit()
    quit('Fail')
