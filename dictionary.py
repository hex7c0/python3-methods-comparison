#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
https://wiki.python.org/moin/PythonSpeed/PerformanceTips#Initializing_Dictionary_Elements

It's important to catch the expected KeyError exception,
and not have a default except clause to avoid trying to recover from an exception
you really can't handle by the statement(s) in the try clause.

@author hex7c0 <hex7c0@gmail.com>
'''

import timeit
dic = {'0':0, '1':11, '2':33, '4':44, '5':55, '6':66, '7':77, '8':88, '9':99, '0':0, 'ciao':'come', 'foo':'pippo'}

def normal():

    wdict = {}

    for word in dic:
        if word not in wdict:
            wdict[word] = 0
        wdict[word] += 1
    return wdict

def exception():

    wdict = {}

    for word in dic:
        try:
            wdict[word] += 1
        except KeyError:
            wdict[word] = 1
    return wdict

def get():

    wdict = {}
    get = wdict.get

    for word in dic:
        wdict[word] = get(word, 0) + 1
    return wdict

def default():

    from collections import defaultdict
    wdict = defaultdict(int)

    for word in dic:
        wdict[word] += 1
    return wdict

if __name__ == '__main__':

    jointimer = timeit.Timer('normal()', 'from __main__ import normal')
    print ('Normal method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('exception()', 'from __main__ import exception')
    print ('Exception method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('get()', 'from __main__ import get')
    print ('Get method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('default()', 'from __main__ import default')
    print ('Default method took %f seconds' % jointimer.timeit())

    # test
    if(normal() == exception() == get() == default()):
        quit()
    quit('Fail')
