#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:csvDemo.py

import csv

#def csvDemo():
rowlist=[]
with open('aaa.csv','rb') as csvopen:
    csvread=csv.reader(csvopen,dialect='excel')
    for row in csvread:
         rowlist.append(row)

for i in range(len(rowlist))[1:]:
    print rowlist[i]

