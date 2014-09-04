#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
https://wiki.python.org/moin/PythonSpeed/PerformanceTips#Import_Statement_Overhead

It's often useful to place them inside functions to restrict their visibility
and/or reduce initial startup time.
Although Python's interpreter is optimized to not import the same module multiple times,
repeatedly executing an import statement can seriously affect performance in some circumstances.

@author hex7c0 <hex7c0@gmail.com>
'''

import timeit

def normal():

    import os
    import hashlib
    import random

    def a():
        os.getcwd()
        hashlib.new('md5')
        random.randrange(0, 9)
        return

    def b():
        os.getcwd()
        hashlib.new('md5')
        random.randrange(0, 9)
        return

    a()
    b()
    del os, hashlib, random
    return

def inside():

    def a():
        import os
        import hashlib
        import random

        os.getcwd()
        hashlib.new('md5')
        random.randrange(0, 9)

        del os, hashlib, random
        return

    def b():
        import os
        import hashlib
        import random

        os.getcwd()
        hashlib.new('md5')
        random.randrange(0, 9)
        del os, hashlib, random
        return

    a()
    b()
    return

if __name__ == '__main__':

    jointimer = timeit.Timer('normal()', 'from __main__ import normal')
    print ('Normal method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('inside()', 'from __main__ import inside')
    print ('Inside method took %f seconds' % jointimer.timeit())
