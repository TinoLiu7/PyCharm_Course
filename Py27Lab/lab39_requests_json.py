import requests

url1 = 'https://bugzilla.mozilla.org/rest/bug/35'
r1 = requests.get(url1)
print r1.status_code, type(r1.content), type(r1.json())
allBugs = r1.json()['bugs']
firstBug = allBugs[0]
for k, v in firstBug.items():
    print 'key=%s, value=%s' % (str(k), str(v))
ccDetails = firstBug['cc_detail']
for ccDetail in ccDetails:
    for k1, v1 in ccDetail.items():
        print 'inside ccdetail, key=%s, value=%s'%(k1, v1)