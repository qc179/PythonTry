#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:input_output_file 
#练习可以使用命令行参数的python程序

import sys,getopt

def infoutf(argv):
    inputfile = ""
    outputfile = ""

    try:
        #用到了getopt模块的getopt方法
        #hio是三个选项，:表示后面需有参数，长选项可选
        #选项和参数以[('-i', '99'), ('-o', '88')]的形式赋值给opts
        #aa的意义不明
        opts,aa = getopt.getopt(argv,"hi:o:",["infile=","outfile="])
    except getopt.GetoptError:
        print 'Error: test_arg.py -i <inputfile> -o <outputfile>'
        print ' or: test_arg.py --infile=<inputfile> --outfile=<outputfile>'
        sys.exit(2)

    #opt表示选项，arg表示参数，aa的作用可能是getopt的使用规则需要
    for opt,arg in opts:
        if opt == "-h":
            print 'test_arg.py -i <inputfile> -o <outputfile>'
            print 'or: test_arg.py --infile=<inputfile> --outfile=<outputfile>'
            sys.exit()
        elif opt in ("-i","--infile"):
            inputfile = arg
        elif opt in ("-o", "--outfile"):
            outputfile = arg

    print 'input file:',inputfile
    print 'output file:',outputfile

if __name__=="__main__":
    infoutf(sys.argv[1:])
#__name__，
#如果是放在Modules模块中，就表示是模块的名字；
#如果是放在Classs类中，就表示类的名字；
#为避免当前内容被作为模块被调用时重复运行，如：import infoutf
#则 infoutf.__name__=='infoutf'

#import os
#print 'number of arguments:',len(sys.argv)
#print 'they are:',str(sys.argv)
