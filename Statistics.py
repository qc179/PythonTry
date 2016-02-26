#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Statistics of each word
#There are two modes in this script
#Mode 1 : Statistic a string by English or Chinese
#Mode 2 : Statistic a string all by English words
#Enter 'q' or 'n' to quit

def S1(n):
  n=unicode(n.replace(' ',''),'utf-8')
  nlen=len(n)
  a=[]
  for i in range(nlen):
    if n[i] in a:
      continue
    else:
      a.append(n[i])
      print n[i],n.count(n[i])
  return ''

def S2(n):
  n=n.strip()
  blank=[0,len(n)]
  word=[]
  worded=[]
  for i in range(len(n)):
    if n[i]==' ' and n[i+1]==' ':
      continue
    if n[i]==' ':
      blank.insert(-1,i)
# print blank
  while len(blank) != 1:
    word.append(n[blank[0]:blank[1]].strip())
    del blank[0]
  for w in word:
    if w in worded:
      continue
    else:
      worded.append(w)
      print w,word.count(w)
  return ''

while True:
  choose=raw_input('Choose one way to run , S1 or S2 : ')
  if choose in ('S2','2'):
    n=raw_input('You can enter a string only including English and more \
than one word : ')
    print S2(n)
    break
  elif choose in ('S1','1'):
    n=raw_input('You can enter a string including any word : ')
    print S1(n)
    break
  elif choose in ('quit','q','n'):
    break
  else:
    print 'You can only input S1 or S2 . Read this file to get more \
info .'
    continue

