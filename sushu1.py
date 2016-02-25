#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Filename:sushu1.py

n=int(raw_input('请输入一个数作为N，将生成0-N间的素数：'))+1
slist=[]
for i in range(2,n):
  for num in range(2,i+1):
    if i % num == 0 and i != num:
      break
    if i % num !=0:
      continue
    slist.append(i)

print slist
#整除且两数不相等，跳出
#不整除则返回继续下一轮循环
#continue是为了返回继续遍历其他的num
#如果遍历完全部的(2,i+1)都没有出现break
#一直遍历到i=num就执行print
#整个过程就是找能整除自己且不等的数
#没找到就继续一个一个试，一直试到自己就是素数
#    o=i%num
#    print i,'%',num,'=',o

