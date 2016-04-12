#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:pg.py

import psycopg2 as pg2

try:
    conn = pg2.connect(database='forummon',user='qiuchen',password='qiuchen'\
    ,host='192.168.1.35',port='5432')
    cur = conn.cursor()
except Exception,e:
    print e

print '123'
# cur = conn.cursor()
# cur.execute('select * from board limit 5')
# rowlist = cur.fetchall()
# for row in rowlist:
#     print row

#close connection
conn.commit()
conn.close()