v1 = 'abcdefg' * 5
v2 = ['a', 'b', 'c']
v3 = list(v1)
print type(v1), type(v2), type(v3), v1, v2, v3
v2[0] = '*'
v2[1] = '@'
v2[2] = '+'
print v2
v3[0:5] = '!'
print v3
del v3[0:5]
print v3
v3[0:5] = []
print v3
