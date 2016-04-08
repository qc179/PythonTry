#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:xlsDemo.py

import os,time

try:
    import xlrd
except Exception, e:
    print ' Start to setup module xlrd.\n'
    os.chdir('xlrd-0.9.4')
    os.system('python setup.py install')
    print '\n Finished.'
else:
    print '\n The module xlrd was already exists.'

time.sleep(1)
getany = raw_input('\n press Enter to quit. ')
    