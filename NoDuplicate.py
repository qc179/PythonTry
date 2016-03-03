#!/usr/bin/env python
#-*- coding: utf-8 -*-

#A function to delete duplicate words in a string

text=raw_input('enter something :')

wordlist=text.split()
wordlist=set(wordlist)
f=open('nodup','w')
for w in wordlist:
    f.write(w+'\n')
f.close()

f=open('nodup','r')
p=f.read()
print p
f.close()
