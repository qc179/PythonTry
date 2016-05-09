#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:checkboard.py

import sys
sys.path.append('mod')
import xlrd
import xlwt
import psycopg2 as pg2
import getcfg

cfg = getcfg.getcfg('checkboard.cfg')

#make board source into a list from sheet1
board = xlrd.open_workbook('board.xls')
bsheet1 = board.sheets()[0]
srclist = []
for row in range(bsheet1.nrows)[1:]:
    values = []
    for col in range(bsheet1.ncols):
        values.append(bsheet1.cell(row,col).value)
    srclist.append(values)

#try connect database
try:
    conn = pg2.connect(
    database=cfg['database'],
    user=cfg['user'],
    password=cfg['password'],
    host=cfg['host'],
    port=cfg['port']
    )
except Exception,e:
    #print e
    print 'Connect server failed.'
    anyenter = raw_input('Press ENTER to quit.')

#make cursor of connection 'conn'
cur = conn.cursor()

#init result.xls such as title and column width
initsave = xlwt.Workbook(encoding='utf-8')
isheet1 = initsave.add_sheet('sheet1')
isheet1.write(0,0,'Fid')
isheet1.write(0,1,'Name')
isheet1.write(0,2,'Url')
isheet1.write(0,3,'Bid')
isheet1.write(0,4,'Status')
isheet1.write(0,5,'Count')
isheet1.col(2).width = 256*50
isheet1.col(1).width = 256*15

#judge each source whether has been inserted , then save it
print 'There are {} boards need to be checked ..'.format(len(srclist))
print '*'*78
rows = 1
for eachsrc in srclist:
    #eachsrc[0]:board name
    #eachsrc[1]:board url
    sql0 = "select fid,name,url,bid from board where is_active=1 \
    and name~'"+eachsrc[0]+"' and url='"+eachsrc[1]+"' order by bid"
    cur.execute(sql0)
    anslist = cur.fetchall()
    #anslist:a list of select results    
    if len(anslist) == 0:
        #isheet1.write(rows,0,'NONE')
        isheet1.write(rows,1,eachsrc[0])
        isheet1.write(rows,2,eachsrc[1])
        # isheet1.write(rows,3,'NONE')
        isheet1.write(rows,4,'未配置')
        isheet1.write(rows,5,len(anslist))
        print 'complete {}/{}.'.format(rows,len(srclist))
        rows = rows+1
    else:
        ans = anslist[0]
        isheet1.write(rows,0,ans[0])
        isheet1.write(rows,1,ans[1])
        isheet1.write(rows,2,ans[2])
        isheet1.write(rows,3,ans[3])
        isheet1.write(rows,4,'OK')
        isheet1.write(rows,5,len(anslist))
        print 'complete {}/{}.'.format(rows,len(srclist))
        rows = rows+1

initsave.save('result.xls')

conn.commit()
conn.close()
print '*'*78
anyenter = raw_input('Check result has been saved.Press Enter to quit.')