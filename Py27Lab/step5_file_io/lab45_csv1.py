import csv
sampleFile1 = open('.\\data\\data1.csv')
sampleReader = csv.reader(sampleFile1)
sampleData = list(sampleReader)
sampleFile1.close()

print type(sampleData)
for row in sampleData:
    for col in row:
        print col,
        pass
    print 'end of row'