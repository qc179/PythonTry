#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:xlsDemo.py

import os,time

try:
	import xlrd
except Exception, e:
	print 'Start to setup module xlrd .\n'
	os.chdir('xlrd-0.9.4')
	cwd = os.getcwd()
	print cwd
	# os.system('python setup.py install')
else:
	print '\nThe module xlrd was already exists .\n'

time.sleep(2)
getany = raw_input('Enter any to exit now : ')