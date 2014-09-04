#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Simple way to comparison speed of python hashlib functions

@author hex7c0 <hex7c0@gmail.com>
'''

import hashlib
import timeit

def md4(s):
    h = hashlib.new('md4')
    h.update(s.encode())
    return h.hexdigest()

def md5(s):
    h = hashlib.new('md5')
    h.update(s.encode())
    return h.hexdigest()

def sha(s):
    h = hashlib.new('sha')
    h.update(s.encode())
    return h.hexdigest()

def sha1(s):
    h = hashlib.new('sha1')
    h.update(s.encode())
    return h.hexdigest()

# python3.4.0b1
# def sha3_256( s ):
#     h = hashlib.new( 'sha3_256' )
#     h.update( s.encode() )
#     return h.hexdigest()

def ripemd160(s):
    h = hashlib.new('ripemd160')
    h.update(s.encode())
    return h.hexdigest()

def dsa(s):
    h = hashlib.new('DSA')
    h.update(s.encode())
    return h.hexdigest()

if __name__ == '__main__':

    jointimer = timeit.Timer('md4("ciao")', 'from __main__ import md4')
    print ('md4 method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('md5("ciao")', 'from __main__ import md5')
    print ('md5 method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('sha("ciao")', 'from __main__ import sha')
    print ('sha method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('sha1("ciao")', 'from __main__ import sha1')
    print ('sha1 method took %f seconds' % jointimer.timeit())

    # python3.4.0b1
    # jointimer = timeit.Timer( 'sha3_256("ciao")', 'from __main__ import sha3_256' )
    # print ( 'sha3_256 method took %f seconds' % jointimer.timeit() )

    jointimer = timeit.Timer('ripemd160("ciao")', 'from __main__ import ripemd160')
    print ('ripemd160 method took %f seconds' % jointimer.timeit())

    jointimer = timeit.Timer('dsa("ciao")', 'from __main__ import dsa')
    print ('dsa method took %f seconds' % jointimer.timeit())
