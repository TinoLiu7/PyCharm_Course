from datetime import datetime

now = datetime.now()
print "repr:" + repr(now)
print "str:" + str(now)
print now, (now)
print [now], (now,), {now}, {'k1': now}
print [str(now)], (str(now),), {str(now)}, {'k1': str(now)}
