# encoding=UTF-8
import os, sys
dirName = '中文目錄'
print(os.getcwd())
os.mkdir(dirName)
os.chdir(dirName)
print(os.getcwd())
os.chdir('..')
os.rmdir(dirName)
print(os.getcwd())
