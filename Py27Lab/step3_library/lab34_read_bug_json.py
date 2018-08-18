import json
import requests

url1 = "https://bugzilla.mozilla.org/rest/bug/35"
r1 = requests.get(url1)
print r1.status_code, type(r1.content), type(r1.json())
print r1.content[:50]
obj_bug_35 = r1.json()
the_bug_35 = obj_bug_35["bugs"][0]
print type(the_bug_35), the_bug_35
bug_35_creator_detail = the_bug_35["creator_detail"]
for k, v in bug_35_creator_detail.items():
    print 'key=', k, " ,value=", v
bug_35_cc_detail = the_bug_35["cc_detail"]
#for cc in bug_35_creator_detail:
for cc in bug_35_cc_detail:
    for k, v in cc.items():
            print 'k2=', k, ' ,v2=', v
