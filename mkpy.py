#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:mkpy.py

import sys

def mkpy(argv):

    for f in argv:

        filename=str(f)+'.py'
        print 'Create',filename,'complate.'

        mk=open(filename,'w')
        mk.write('#!/usr/bin/env python\n#-*- coding: utf-8 -*-\n#filename:{}\n'.format(filename))
        mk.close()

if __name__=='__main__':
    mkpy(sys.argv[1:])
