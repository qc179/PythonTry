#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:upload_sespider.py

import os

with open('upload_sespider_ip.cfg','rb') as setip:
    iplist = setip.readlines()
    a = []
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
            a.append(iplist[i])
print a

confirm = raw_input('Is IP all right ? Please check it .\nPress ENTER to continue or CTRL+C')
#scp -r /home/shiyanlou/spiders/sespider/ appadmin@211.149.199.70:~/
confirm = []
for i in a:
    cmd='scp -r /home/shiyanlou/spiders/sespider/ appadmin@'+i+':~/'
    print cmd
    os.system(cmd)
