from datetime import datetime

now = datetime.now()

print "repr:", repr(now)
print "str:", str(now)
print "[1] direct print:", now
# in console
# now
print (now,)
print [now, ]
print {now, }
print {'k1': now}
print (str(now),)
print [str(now), ]
print {str(now), }
print {'k1': str(now)}
