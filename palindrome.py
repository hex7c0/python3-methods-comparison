#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Simple way to comparison speed of python reverse string functions

@author hex7c0 <hex7c0@gmail.com>
"""

import hashlib
import timeit



def str_reverse(s):
    return s == s[::-1]

def str_reverse_half(s):
    l = len(s) // 2
    return s[:l]  == s[:l:-1]

def str_reversed(s):
    return s  == ''.join(reversed(s))

def str_reversed_half(s):
    s = s[:len(s) // 2]
    return s  == ''.join(reversed(s))


if __name__ == '__main__':

    jointimer = timeit.Timer('str_reverse("Radar")', 'from __main__ import str_reverse')
    print ('str_reverse method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('str_reverse_half("Radar")', 'from __main__ import str_reverse_half')
    print ('str_reverse_half method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('str_reversed("Radar")', 'from __main__ import str_reversed')
    print ('str_reversed method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('str_reversed_half("Radar")', 'from __main__ import str_reversed_half')
    print ('str_reversed_half method took %f seconds' % jointimer.timeit())
