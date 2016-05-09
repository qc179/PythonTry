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

inittieba = xlwt.Workbook(encoding='utf-8')
tieba = inittieba.add_sheet('sheet1')
tieba.write(0,0,'Name')
tieba.write(0,1,'Url')
tieba.write(0,2,'Status')
tieba.col(1).width = 256*50
tieba.col(0).width = 256*15

#judge each source whether has been inserted , then save it
print 'There are {} boards need to be checked ..'.format(len(srclist))
print '*'*75
rows = 1
for eachsrc in srclist:
    #eachsrc[0]:board name
    #eachsrc[1]:board url
    print 'Source number:',rows
    istieba = re.match('http://tieba\.baidu\.com.*',eachsrc[1])
    if istieba:
        namelen = len(eachsrc[0])
        namelast = eachsrc[0][namelen-1]
        urlfmt = re.match('^http://tieba\.baidu\.com/f\?kw=[A-za-z0-9%]+$',\
            eachsrc[1])
        if namelast != u'吧' :
            tieba.write(rows,0,eachsrc[0])
            tieba.write(rows,1,eachsrc[1])
            tieba.write(rows,2,u'吧名不规范，请检查')
        else :
            if urlfmt:
                tieba.write(rows,0,eachsrc[0])
                tieba.write(rows,1,eachsrc[1])
                tieba.write(rows,2,u'吧名和URL正确')
            else:
                tieba.write(rows,0,eachsrc[0])
                tieba.write(rows,1,eachsrc[1])
                tieba.write(rows,2,u'URL不规范，请检查')

    else:
        tieba.write(rows,0,eachsrc[0])
        tieba.write(rows,1,eachsrc[1])
        tieba.write(rows,2,u'非贴吧URL')
    rows = rows+1

inittieba.save('tiebaresult.xls')

print '*'*75
anyenter = raw_input('Check result has been saved.Press Enter to quit.')
