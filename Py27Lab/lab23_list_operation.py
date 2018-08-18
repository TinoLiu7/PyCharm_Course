dayOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

lengthArray = []
for day in dayOfWeek:
    lengthArray.append(len(day))
    pass
print lengthArray

print [len(day) for day in dayOfWeek]

sun, mon, tue, wed, thr, fri, sat = dayOfWeek
print sun, wed, fri
print mon, thr, sat