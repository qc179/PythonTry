#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:os.walk.py

import os

def filewalk():
    for root, dirs, files in os.walk(".", topdown=True):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))

if __name__=='__main__':
    filewalk()
