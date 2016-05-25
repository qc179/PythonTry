#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:checknews.py


import sys
sys.path.append('mod')
import xlrd
import xlwt
import psycopg2 as pg2
import getcfg
import re

cfg = getcfg.getcfg('checkboard.cfg')

#try connect database
try:
    conn = pg2.connect(
    database=cfg['database'],
    user=cfg['user'],
    password=cfg['password'],
    host=cfg['host'],
    port=cfg['port']
    )
    cur = conn.cursor()
except Exception,e:
    #print e
    print 'Connect server failed.'
    anyenter = raw_input('Press ENTER to quit.')

#make news source into a list from sheet1
news = xlrd.open_workbook('news.xls')
bsheet1 = news.sheets()[0]
srclist = []
for row in range(bsheet1.nrows)[1:]:
    values = []
    for col in range(bsheet1.ncols):
        values.append(bsheet1.cell(row,col).value)
    srclist.append(values)

#init news_result.xls such as title and column width
initsave = xlwt.Workbook(encoding='utf-8')
isheet1 = initsave.add_sheet('sheet1')
isheet1.write(0,0,' ')
isheet1.write(0,1,'Name')
isheet1.write(0,2,'URL')
isheet1.write(0,3,'Fid')
isheet1.write(0,4,'Bid')
isheet1.write(0,5,'Count')
isheet1.write(0,6,'Status')
isheet1.write(0,7,'SourceName')
isheet1.col(1).width = 256*15
isheet1.col(2).width = 256*50
isheet1.col(6).width = 256*20
isheet1.col(7).width = 256*15

#judge each source whether has been inserted,then save them
print 'There are {} news need to be checked ..'.format(len(srclist))
print '*'*78
rows = 1
for eachsrc in srclist:
    #eachsrc[0]:news name
    #eachsrc[1]:news url
    istieba = re.match('http://tieba\.baidu\.com.*',eachsrc[1])
    nameblank = re.match('\s+(?u)\w+|(?u)\w+\s+',eachsrc[0])
    urlblank = re.match('\s+.*|.*\s+',eachsrc[1])
    if nameblank or urlblank:
        isheet1.write(rows,1,eachsrc[0])
        isheet1.write(rows,2,eachsrc[1])
        isheet1.write(rows,6,u'Name或URL含有空格，请修改')            
    else:
        sql0 = "select fid,name,url,nsid from news_site where is_active=1 \
        and url='"+eachsrc[1]+"' order by nsid"
        cur.execute(sql0)
        anslist = cur.fetchall()
        #anslist:a list of select results    
        if len(anslist) == 0:
            #isheet1.write(rows,3,'NONE')
            isheet1.write(rows,1,eachsrc[0])
            isheet1.write(rows,2,eachsrc[1])
            # isheet1.write(rows,4,'NONE')
            isheet1.write(rows,6,u'未查到这个URL')
            isheet1.write(rows,5,len(anslist))
        else:
            ans = anslist[0]
            isheet1.write(rows,3,ans[0])
            isheet1.write(rows,1,ans[1])
            isheet1.write(rows,2,ans[2])
            isheet1.write(rows,4,ans[3])
            #isheet1.write(rows,6,'OK')
            isheet1.write(rows,5,len(anslist))            
            unicodename=ans[1].decode('utf-8')
            if unicodename != eachsrc[0]:
                isheet1.write(rows,6,u'版面已配置但名称不同')
                isheet1.write(rows,7,eachsrc[0])
            else:
                pass
    print 'complete {}/{}.'.format(rows,len(srclist))
    rows = rows+1

initsave.save('news_result.xls')

conn.commit()
conn.close()
print '*'*78
anyenter = raw_input('Check result has been saved.Press Enter to quit.')
