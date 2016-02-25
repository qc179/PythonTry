name=raw_input('Please input your name,I will remember it,just here:')
name=name.strip()
name=name.title()
if name=='':
    print 'You kidding me?'
elif name.isdigit():
    print 'Really?You are digital man,hah?'
else:
    print '\n'+'*'*30
    print 'OK,I get it,your name is {}.\nHi {},nice to meet you.'.format(name,name)
    print '*'*30+'\n'
