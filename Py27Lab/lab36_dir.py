# encoding=UTF-8
import os, sys
dirName = u'中文目錄'
print os.getcwd()
os.mkdir(dirName)
os.chdir(dirName)
print os.getcwd().decode('ms950')
os.chdir('..')
os.rmdir(dirName)
print os.getcwd()
