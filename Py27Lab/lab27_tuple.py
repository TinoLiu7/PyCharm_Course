day_of_week = ('Sunday', 'Monday', 'Tuesday')
print type(('Wednesday')), type(('Wednesday',))
day_of_week += ('Wednesday',)
print day_of_week
print ('Wednesday') * 5
print ('Wednesday',) * 5


def split_head(seq):
    return seq[0], seq[1:]
dayOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
head, remaining = split_head(dayOfWeek)
print 'remaining=',remaining
print 'head=', head
