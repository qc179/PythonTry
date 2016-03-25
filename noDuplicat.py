#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Filename:noDuplicate.py

import os

def noduplicate():
    """A function to delete duplicate words in a string"""
    text=raw_input('enter something :')
    wordlist=text.split()
    wordlist=set(wordlist)

    f=open('nodup.tmp','w')
    for w in wordlist:
        f.write(w+'\n')
    f.close()

    f=open('nodup.tmp','r')
    p=f.read()
    print p
    f.close()

    os.remove('nodup.tmp')

if __name__=='__main__':
    noduplicate()
