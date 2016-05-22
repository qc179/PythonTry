#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:averaged.py
#Auto grouped weibo's bid averaged before init

import xlrd
from collections import deque

getbids = xlrd.open_workbook('weibo_bids.xls')
bids_sheet1 = getbids.sheets()[0]
bids_list = []
for row in range(bids_sheet1.nrows):
    #把bid化整后字符串化
    bid = str(int(bids_sheet1.cell(row,0).value))
    #把文章数化整
    artnum = int(bids_sheet1.cell(row,1).value)
    #添加到列表
    bids_list.append((bid,artnum))
#转换成字典
bids_dict = dict(bids_list)
print 'bids_dict len:',len(bids_dict)

key_list = bids_dict.keys()
print '\nkeys list len:',len(key_list)

val_list = bids_dict.values()
val_list_len = len(val_list)
print '\nvalues list leng :',val_list_len

val_sum = sum(val_list)
print '\nvalues sum =',val_sum

val_list.sort(reverse=True)
val_queue = deque(val_list)

print u'\n需要均分为几组：'
spider_num = raw_input()
spider_num = int(spider_num)

avg_target = val_sum/spider_num
print u'目标均值：',avg_target,'\n'

group = []
group_num = 0
while len(val_queue)>0:
    group_len = len(group)
    if group_len == 0:
        group_sum = 0
    else:
        group_sum = sum(group)

    if group_num == val_list_len:
        print group
        print u'---单组合计',group_sum,u'相差均值',group_sum-avg_target
        print u'共',group_num,u'个数值，全部完成均分'
        break
    elif abs(avg_target-group_sum) < min(val_queue):
        print group
        print u'--单组合计',group_sum,u'相差均值',group_sum-avg_target
        group = []
    elif group_sum >= avg_target:
        print group
        print u'-单组合计',group_sum,u'相差均值',group_sum-avg_target
        group = []


    if len(val_queue) == 1:
        cur = val_queue.popleft()
        group.append(cur)
        group_num += 1
        print group
        print u'---单组合计',sum(group),u'相差均值',sum(group)-avg_target
        print u'\n共',group_num,u'个数值，全部完成均分'
        break
    else:
        cur = val_queue.popleft()
        if cur >= avg_target:
            group.append(cur)
            group_num += 1
            print group
            print u'大于均值 相差均值',sum(group)-avg_target
            group = []
            continue
        else:
            curx = abs(avg_target-group_sum-cur)
            oxlist = [abs(avg_target-group_sum-o) for o in val_queue]
            ox = min(oxlist)
            if curx <= ox:
                group.append(cur)
                group_num += 1
            else:
                val_queue.append(cur)

print '*'*75
anyenter = raw_input('Grouped completed.Press Enter to quit.')