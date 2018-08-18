dayOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
dayOfWeekT = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
print dayOfWeek

wordLengths = []
for day in dayOfWeek:
    wordLengths.append(len(day))

print wordLengths

print [len(day) for day in dayOfWeek]
print [len(day) for day in dayOfWeekT]

sun, mon, tue, wed, thr, fri, sat = dayOfWeekT
print sun, tue, thr
print mon, wed, fri, sat