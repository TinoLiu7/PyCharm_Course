sales = {'iphone6': 500, 'iphone6+': 400, 'iphone7': 500, 'iphone7+': 200}
print sales['iphone6+']
sales['iphone6']=800
print sales
#print sales['HTC']
print sales.get('HTC')
for item in sales:
    print item, sales[item]
for item in sales.keys():
    print item
for item in sales.values():
    print item
for item in sales.items():
    print item[0], '-----', item[1]
for k,v in sales.items():
    print k, '||||', v
sales['iPad']=150
sales.update({'iphone6':550,'ipad':200})
del sales['iphone7'], sales['iphone7+']
print sales