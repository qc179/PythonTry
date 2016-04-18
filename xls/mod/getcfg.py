#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:getcfg.py

def getcfg(filename):
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
    return a

if __name__ == '__main__':
    a = getlogin('checkboard.cfg')
    print a
