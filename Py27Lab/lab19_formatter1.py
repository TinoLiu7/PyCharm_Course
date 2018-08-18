# encoding=UTF-8
r1 = 5
area1 = r1 * r1 * 3.14159
str1 = 'radius=%.1f, area=%.3f'
print str1 % (r1, area1)
str2 = 'radius=%(radius).1f, area=%(area).3f'
print str2 % {'area': area1, 'radius': r1}
str3 = 'radius={:.1f}, area={:.3f}'
print str3.format(r1, area1)
str4 = 'radius={1:.1f}, area={0:.3f}'
print str4.format(area1, r1)
str5 = '半徑={radius:.1f}, 面積={area:.3f}'
print str5.format(radius=r1, area=area1)