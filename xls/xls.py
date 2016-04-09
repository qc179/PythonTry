#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:xls.py

import xlrd

wb = xlrd.open_workbook('aaa.xls')
sheet1 = wb.sheets()[0]
table = []

for row in range(sheet1.nrows)[1:]:
    values = []
    for col in range(sheet1.ncols):
        if col == 0:
            values.append(int((sheet1.cell(row,col).value)))
        else:
            values.append(sheet1.cell(row,col).value)
    table.append(values)


for a in table:
    select = "select * from baord where fid="+str(a[0])+" and name='"+a[1]+"' and url='"+a[2]+"' and is_active=1"
    print select

anyenter = raw_input('press Enter to quit.')
