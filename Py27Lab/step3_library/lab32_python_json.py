# encoding=UTF-8
import json

data1 = ["Sunday", u'周一', 'Tuesday', 100, 3.14, None]
print type(data1), data1
return1 = json.dumps(data1)
print type(return1), return1
object1 = json.loads(return1)
print type(object1), object1[1]  # 2nd
data2 = {'course': 'BDPY', 'duration': 35, 'instructor': 'Mark',
         'attendee': 40, 'lab': 17.5}
print type(data2), data2
return2 = json.dumps(data2)
print type(return2), return2
object2 = json.loads(return2)
print type(object2), object2['lab'], object2['instructor']
