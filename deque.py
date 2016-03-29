#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:deque.py

from collections import deque

def dequeDemo():
    a = deque([101,102,103,4,5,6,57,58,59])
    file=[]
    dict=[]
    while len(a) > 0:
        b = a.popleft()
        if b > 50:
            dict.append(b)
            b = b-50
            a.append(b)
        else:
            file.append(b)
        print 'A IN QUE:',a
        print 'a<50 is file:',file
        print 'a>50 is dict:',dict

if __name__=='__main__':
    dequeDemo()
