sales1 = {'iphone6': 500, 'iphone6+': 400, 'iphone7': 300, 'iphoneX': 150}
print type(sales1), len(sales1), sales1['iphone7']
# print sales1['htc']
print sales1.get('iphone7'), sales1.get('apple watch')
print sales1.keys()
print sales1.values()
# print sales1.items()
for item in sales1.items():
    print type(item), item[0], item[1]
    pass
for k, v in sales1.items():
    print k, v
for d in sales1:
    print "when iterate, d=%s" % (d)
for e in sales1.keys():
    print "when iterate key, d=%s" % (e)
