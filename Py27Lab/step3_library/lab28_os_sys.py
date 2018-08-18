#encoding=UTF-8
import os, sys
print os.getcwd()
os.mkdir('foo')
os.chdir('foo')
print os.getcwd()
os.chdir('..')
os.rmdir('foo')
os.mkdir(u'中文')
os.chdir(u'中文')
print os.getcwd().decode('ms950')
os.chdir('..')
os.rmdir(u'中文')
print sys.executable
for item in sys.argv:
    print item