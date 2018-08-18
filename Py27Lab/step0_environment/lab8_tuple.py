a = 5
b = 9
print 'a=', a, ',b=', b
temp = a
a = b
b = temp
print 'a=', a, ',b=', b
c = 2.0
d = 3.14
print 'c=', c, ',d=', d
c, d = d, c
print 'c=', c, ',d=', d
f = 1234.5
g = 'hello world'
print 'f=', f, ',g=', g
f, g = g, f
print 'f=', f, ',g=', g
a = 500
b = 3.14
c = 'hello world'
a, b, c = c, a, b
print 'a=', a, ',b=', b, ',c=', c
