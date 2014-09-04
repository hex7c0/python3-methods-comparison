#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
https://wiki.python.org/moin/PythonSpeed/PerformanceTips#String_Concatenation

In the plus column, strings can be used as keys in dictionaries
and individual copies can be shared among multiple variable bindings.

@author hex7c0 <hex7c0@gmail.com>
'''

import timeit

def normal(s, i):
    return '/user/'

def join_test(s, i):
    return ''.join(['/user/', s, '/', str(i), '/'])

def format_test(s, i):
    return "/user/%s/%i/" % (s, i)

def plus_test(s, i):
    return '/user/' + s + '/' + str(i) + '/'

if __name__ == '__main__':

    jointimer = timeit.Timer('normal("test", 5)', 'from __main__ import normal')
    print ('Normal method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('join_test("test", 5)', 'from __main__ import join_test')
    print ('Join method took %f seconds' % jointimer.timeit())

    formattimer = timeit.Timer('format_test("test", 5)', 'from __main__ import format_test')
    print ('Format method took %f seconds' % formattimer.timeit())

    plustimer = timeit.Timer('plus_test("test", 5)', 'from __main__ import plus_test')
    print ('Plus method took %f seconds' % plustimer.timeit())

    # test
    if(normal("test", 5) != join_test('test', 5) == format_test('test', 5) == plus_test('test', 5)):
        quit()
    quit('Fail')