r = 2
a = r * r * 3.14
print r, a
str1 = 'radius=%f, area=%f'
print str1 % (r, a)
str2 = 'radius=%.2f, area=%.2f'
print str2 % (r, a)
str3 = 'radius=%(radius).2f, area=%(area).2f'
print str3 % {'radius': r, 'area': a}
print str3 % {'area': a, 'radius': r}
str4 = 'radius={}, area={}'
print str4.format(r, a)
str5 = 'radius={:.2f}, area={:.2f}'
print str5.format(r, a)
str7 = 'radius={0:.2f}, area={1:.2f}'
print 'type7', str7.format(r, a)
str8 = 'radius={1:.2f}, area={0:.2f}'
print 'type8', str8.format(a, r)
str6 = 'radius={radius:.2f}, area={area:.2f}'
print str6.format(radius=r, area=a)
str9 = 'radius={radius:.2f}, area={area:.2f}'
print str6.format(area=a, radius=r)
