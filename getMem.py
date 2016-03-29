#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:getMem.py

import time

def getMem():
    """Get information of memmory."""
    with open('/proc/meminfo') as f:
        total = int(f.readline().split()[1])
        free = int(f.readline().split()[1])
        buffers = int(f.readline().split()[1])
        cache = int(f.readline().split()[1])
    mem_use=total-free-buffers-cache
    with open ('/var/tmp/mem.log','a')as l:
        l.write(time.ctime()+'\n')
        l.write('Total: '+str(total/1024)+' MB\n')
        l.write('Free: '+str(free/1024)+' MB\n')
        l.write('Buffers: '+str(buffers/1024)+' MB\n')
        l.write('Cache: '+str(cache/1024)+' MB\n')
        l.write('Mem_use: '+str(mem_use/1024)+' MB\n\n')
    print mem_use/1024,'MB'

if __name__=='__main__':
    while True:
        time.sleep(2)
        getMem()
