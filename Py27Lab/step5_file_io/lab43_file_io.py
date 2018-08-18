file1 = open('.\\data\\Python_Introduction', 'r')  # the file is open for read
readme_txt = file1.read()
print type(readme_txt), len(readme_txt), readme_txt[:100]
file1.close()

with open('.\\data\\Python_Introduction', 'r') as file2:
    readme_txt2 = file2.read().decode('UTF-8')
    print type(readme_txt2), len(readme_txt2), readme_txt2[:100]
    pass

file3 = open('.\\data\\clone1', 'w')  # the file is open for write
file3.write(readme_txt)
file3.close()

with open('.\\data\\clone2', 'w') as file4:
    file4.write(readme_txt2.encode('utf-8'))
