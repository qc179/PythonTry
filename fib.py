#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Filename:fib.py
def fib1(n):
	"""Return a list containing the Fibonacci series up to n."""
	c=[]
	a,b=0,1
	while a<n:
		c.append(a)
		a,b=b,a+b
	return c

def fib2(n):
	c=[]
	a,b=0,1
	for i in range(n):
		c.append(a)
		a,b=b,a+b
	return c

while 2>1:
	choose=raw_input('选择一种方式:f1 or f2.按n退出:')
	if choose=='f1':
		n=int(raw_input('请输入数列的上限:'))
		print fib1(n)
		break
	elif choose=='f2':
		n=int(raw_input('请输入数列的数量:'))
		print fib2(n)
		break
	elif choose in ('n','no','quit','exit'):
		break
	else:
		print 'Please make the right choice!'
		

#n=int(raw_input('Please set series\'s quantity:'))
#n=int(raw_input('Please set series\'s upper limit:'))
#n=int(n)


