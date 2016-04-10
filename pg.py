#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:pg.py

import psycopg2 as pg2

conn = pg2.connect(database='forummon',user='qiuchen',password='qiuchen'\
    ,host='192.168.1.35',port='5432')

print 'conn ok'

cur = conn.cursor()
cur.execute('select * from board limit 5')
rowlist = cur.fetchall()
for row in rowlist:
    print row

#close connection
conn.commit()
conn.close()