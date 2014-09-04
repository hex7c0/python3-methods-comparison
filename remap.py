#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
https://wiki.python.org/moin/PythonSpeed/PerformanceTips#Re-map_Functions_at_runtime

It's important to catch the expected KeyError exception,
and not have a default except clause to avoid trying to recover from an exception
you really can't handle by the statement(s) in the try clause.

@author hex7c0 <hex7c0@gmail.com>
'''

import timeit

def normal():

    class Test(object):
        def check(self, a, b, c):
            if(a == 0):
                self.str = b * 10
            else:
                self.str = c * 10
            return

    a = Test()
    for i in range(0, 10):
        a.check(i, 'b', 'c')
    return

def remap():

    class Test(object):
        def check(self, a, b, c):
            self.str = b * 10
            self.check = self.check_post  # remap check fx
            return
        def check_post(self, a, b, c):
            self.str = c * 10
            return

    a = Test()
    for i in range(0, 10):
        a.check(i, 'b', 'c')
    return

if __name__ == '__main__':

    jointimer = timeit.Timer('normal()', 'from __main__ import normal')
    print ('Normal method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('remap()', 'from __main__ import remap')
    print ('Remap method took %f seconds' % jointimer.timeit())
