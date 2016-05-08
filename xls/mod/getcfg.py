#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:getcfg.py

def getcfg(filename):
    try:
        with open(filename,'rb') as cfg:
            cfglist = cfg.readlines()
            a = []
            for i in range(len(cfglist)):
                cfglist[i] = cfglist[i].replace('\r','')
                cfglist[i] = cfglist[i].replace('\n','')
                cfglist[i] = cfglist[i].replace(' ','')
                cfglist[i] = cfglist[i].split('=')
                a.append((cfglist[i][0],cfglist[i][1]))
        a = dict(a)
    except Exception,e:
        print e
        print 'Please check checkboard.cfg,it looks like something wrong.'
        anyenter = raw_input('Press ENTER to confirm.')
    return a

if __name__ == '__main__':
    a = getcfg('checkboard.cfg')
    print a
