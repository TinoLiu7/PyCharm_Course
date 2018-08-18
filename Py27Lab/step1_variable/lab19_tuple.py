dayOfWeekT = ('Sunday', 'Monday')
# dayOfWeekT += ('Tuesday')
dayOfWeekT += ('Tuesday',)
print dayOfWeekT
print type(('Tuesday')), type(('Tuesday',))
print ('Wednesday') * 3
print ('Wednesday',) * 3
print dayOfWeekT[2], dayOfWeekT[-2]
print 'day' in dayOfWeekT
print 'Sunday' in dayOfWeekT


def splitHead(x):
    return x[0], x[1:]


dayOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print splitHead(dayOfWeek)[0], type(splitHead(dayOfWeek)[0])
# remaining still a list
print type(splitHead(dayOfWeek)[1])
