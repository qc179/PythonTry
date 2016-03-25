#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename:mkpy.py

import sys,os

def mkpy(argv):

    for f in argv:

        filename=str(f)+'.py'

        mk=open(filename,'w')
        mk.write('#!/usr/bin/env python\n#-*- coding: utf-8 -*-\n#filename:{}\n'.format(filename))
        mk.close()
        os.chmod(filename,0774)
        print 'Create',filename,'complate.'

    print 'Finish.'

if __name__=='__main__':
    mkpy(sys.argv[1:])
