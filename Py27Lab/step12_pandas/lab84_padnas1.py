import pandas
from matplotlib import pyplot, rc

data1 = pandas.read_csv('.\\data\\data1.csv', skiprows=4, index_col='Country Name')
print data1.shape
print data1.head()
print data1.columns
# write out
# pip install openpyxl
data1.to_excel('.\\data\\pandas_output.xlsx', sheet_name='population')
print data1['1960'].mean()
print data1['1970'].mean()
data1['join1980_1990'] = data1['1980'] + data1['1990']
print data1.columns
ausData = data1[data1['Country Code'] == 'AUS']
print ausData.shape
# change font
font = {'family': 'Courier New'}
rc('font', **font)
# get pyplot available styles
print pyplot.style.available
pyplot.style.use('seaborn-dark-palette')
years = ['1960', '1970', '1980', '1990']
# change font size
ausData.plot(kind='bar', y=years, figsize=(12, 6), fontsize=14)
pyplot.show()
