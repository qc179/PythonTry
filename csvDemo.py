#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:csvDemo.py

import csv

#def csvDemo():
#rowlist=[]
with open('aaa.csv','rb') as csvrb:
    csvread=csv.reader(csvrb,dialect='excel')
    rows=[row for row in csvread]
#    for row in csvread:
#         rowlist.append(row)

for i in rows[1:]:
    i[1]=i[1].decode('gbk').encode('utf-8')
    i[2]=i[2].decode('gbk').encode('utf-8')
    for ii in i:
        print ii,
    print '\m'

with open('bbb.csv','ab') as csvab:
    csvwrite=csv.writer(csvab,dialect='excel')
    for i in rows[1:]:
        csvwrite.writerow(i)

quit=raw_input('Enter any word to exit : ')
