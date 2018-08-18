file1 = open(".\\data\\Python_Introduction")
readme_txt = file1.read()
print len(readme_txt), type(readme_txt), readme_txt[:200]
file1.close()

with open(".\\data\\Python_Introduction") as file2:
    readme_txt2 = file2.read().decode('UTF-8')
    print len(readme_txt2), type(readme_txt2), readme_txt2[:200]
# will be close here

file3 = open('.\\data\\clone1', 'w')
file3.write(readme_txt)
file3.close()

with open('.\\data\\clone2','w') as file4:
    file4.write(readme_txt2.encode('UTF-8'))