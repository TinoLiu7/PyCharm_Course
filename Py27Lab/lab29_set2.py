a1 = ('A', 'B', ('A', 'X'))
a2 = ('A', 'C')
s1 = {a1, a2, a1}
print s1
print hex(id(a1[0])), hex(id(a2[0])), hex(id(a1[2][0]))
