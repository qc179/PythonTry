#!/usr/bin/env python
#-*- coding: utf-8 -*-

#A function to delete duplicate words in a string

str=raw_input('enter a string in english :')
wordidx=[]
wordlist=[]
for i in range(len(str)):
  if str[i].isalpha() :
    wordidx.append(i)
    continue
  if len(wordidx)==0 :
    continue
  else:
    if wordidx[0]==wordidx[-1] :
      wordlist.append(str[wordidx[0]])
    else:
      wordlist.append(str[wordidx[0]:wordidx[-1]])
    del wordidx[:]
    continue

print wordlist
