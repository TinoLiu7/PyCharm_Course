import pandas_datareader.wb as wb
data = wb.search(string='SE.PRM.TENR', field='id')
data