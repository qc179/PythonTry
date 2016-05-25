#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:upload_sespider.py

import os

with open('upload_sespider_ip.cfg','rb') as setip:
    iplist = setip.readlines()
    ip = []
    for i in range(len(iplist)):
        if iplist[i] == '\r\n':
            pass
        elif iplist[i] == '\n':
            pass
        elif iplist[i] == '\r':
            pass
        else:
            iplist[i] = iplist[i].replace('\r','')
            iplist[i] = iplist[i].replace('\n','')
            iplist[i] = iplist[i].replace(' ','')
            ip.append(iplist[i])
print ip

#scp -r ~/spiders/sespider/ appadmin@211.149.199.70:~/
#sed -i "s/^spider_group=.*/spider_group=888/g" ~/spiders/sespider_888/sespider.cfg

start = raw_input('请确认IP是否正确,可按 CTRL+C 退出,确认后请输入一个起始Gid：')
for i in ip:
    mvspider = 'mv ~/spiders/sespider_* ~/spiders/sespider_'+str(start)
    os.system(mvspider)

    sedgroup = 'sed -i "s/^spider_group=.*/spider_group='+str(start)+'/g" ~/spiders/sespider_'+str(start)+'/sespider.cfg'
    os.system(sedgroup)

    sedgid = 'sed -i "s/^webmon\.sespider\.gid.*/webmon.sespider.gid='+str(start)+'/g" ~/spiders/sespider_'+str(start)+'/spiderbase.cfg'
    os.system(sedgid)

    upload = 'scp -r ~/spiders/sespider_'+str(start)+' appadmin@'+i+':~/'
    os.system(upload)

    start = int(start)+1
