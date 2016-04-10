#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:checkboard.py

import xlrd
import xlwt
import psycopg2 as pg2
import csv

#get board source from sheet1
board = xlrd.open_workbook('board.xls')
bsheet1 = board.sheets()[0]
srclist = []
for row in range(bsheet1.nrows)[1:]:
    values = []
    for col in range(bsheet1.ncols):
        values.append(bsheet1.cell(row,col).value)
    srclist.append(values)

#connect database
conn = pg2.connect(database='forummon',user='qiuchen',password='qiuchen'\
    ,host='192.168.1.35',port='5432')
cur = conn.cursor()

#init save.xls , insert title
initsave = xlwt.Workbook(encoding='utf-8')
isheet1 = initsave.add_sheet('sheet1')
isheet1.write(0,0,'Fid')
isheet1.write(0,1,'Name')
isheet1.write(0,2,'Url')
isheet1.write(0,3,'Bid')
isheet1.write(0,4,'Status')

#judge each source whether has been inserted , then save it
rows = 1
for eachsrc in srclist:
    #eachsrc[0]:name
    #eachsrc[1]:url
    select = "select fid,name,url,bid from board where is_active=1 \
    and name~'"+eachsrc[0]+"'"
    cur.execute(select)
    anslist = cur.fetchall()
    #anslist:a list of select results    
    if len(anslist) == 0:
        isheet1.write(rows,0,'NONE')
        isheet1.write(rows,1,eachsrc[0])
        isheet1.write(rows,2,eachsrc[1])
        isheet1.write(rows,4,'NONE')
        rows = rows+1
    else:    
        for ans in anslist:
            isheet1.write(rows,0,ans[0])
            isheet1.write(rows,1,ans[1])
            isheet1.write(rows,2,ans[2])
            isheet1.write(rows,3,ans[3])
            isheet1.write(rows,4,'OK')
            rows = rows+1

initsave.save('save.xls')


    # select = "select * from baord where fid="+str(eachsrc[0])+" and name='"\
    # +eachsrc[1]+"' and url='"+eachsrc[2]+"' and is_active=1"
    # print select


conn.commit()
conn.close()

anyenter = raw_input('press Enter to quit.')