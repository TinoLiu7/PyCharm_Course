#encoding=UTF-8
import pandas
data1 = pandas.read_csv('.\\data\\data2_utf8.csv')
print data1.head()
print data1.columns
print data1.info()
data1Grouped = data1[['處分字號','違反勞動基準法條款','違反法規內容']].\
    groupby(['違反勞動基準法條款']).count()
print data1Grouped.head()
data1Grouped.sort_values('處分字號', ascending=False)