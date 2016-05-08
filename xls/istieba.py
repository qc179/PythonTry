#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:istieba.py

import xlrd
import xlwt
import re

#get board source from sheet1
board = xlrd.open_workbook('board.xls')
bsheet1 = board.sheets()[0]
srclist = []
for row in range(bsheet1.nrows)[1:]:
    values = []
    for col in range(bsheet1.ncols):
        values.append(bsheet1.cell(row,col).value)
    srclist.append(values)



#judge each source whether has been inserted , then save it
print 'There are {} boards need to be checked ..'.format(len(srclist))
print '*'*75
rows = 1
for eachsrc in srclist:
    #eachsrc[0]:board name
    #eachsrc[1]:board url
    print 'Source number:',rows
    print 'Name:'+eachsrc[0]
    istieba = re.match('http://tieba\.baidu\.com.*',eachsrc[1])
    if istieba:
        print 'URL:'+eachsrc[1]+' is tieba'
        namelen = len(eachsrc[0])
        namelast = eachsrc[0][namelen-1]
        if namelast == u'吧' :
            print u'yes,it is 吧'
        else :
            #here need update to result after
            print u'吧名末尾不是“吧”字，请修正。'
    else:
        print 'URL:'+eachsrc[1]+' is not a tieba'
    rows = rows+1
    print '\n'



print '*'*75
anyenter = raw_input('Check result has been saved.Press Enter to quit.')
