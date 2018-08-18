import csv
sampleFile1 = open('.\\data\\data2_utf8.csv')
sampleReader = csv.reader(sampleFile1)
sampleData = list(sampleReader)
sampleFile1.close()

print type(sampleData)
for row in sampleData:
    for col in row:
        data1 = col.decode('utf8')
        print type(data1),data1
        pass
    print 'end of row'