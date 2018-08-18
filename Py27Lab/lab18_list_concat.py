a1 = list('abcde')
a2 = list('12345')
a1.append(a2)
print a1
a3 = list('abcde')
a4 = list('12345')
a3.extend(a4)
print a3
a5 = list('abcde')
a6 = list('12345')
a5 += a6
print a5
a6 = list('abcde12345')
a6.reverse()
print a6    