#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:xlsDemo.py
#You need root power when install on linux

import os,time

print '\nChecking module xlrd ..'

try:
    import xlrd
except Exception, e:
    print '\nStart to setup module xlrd ...\n'
    os.chdir('xlrd-0.9.4')
    os.system('python setup.py install')
    print '\nFinished.'
else:
    print '\nThe module xlrd was already exists.'
time.sleep(1)

print '\nChecking module xlwt ..'

try:
    import xlwt
except Exception, e:
    print '\nStart to setup module xlwt ...\n'
    os.chdir('xlwt-1.0.0')
    os.system('python setup.py install')
    print '\nFinished.'
else:
    print '\nThe module xlwt was already exists.'
time.sleep(1)

getany = raw_input('\npress Enter to quit. ')    