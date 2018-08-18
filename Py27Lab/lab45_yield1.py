def functionX():
    a = 1
    b = 1
    yield a
    a += b
    yield a
f1 = functionX()
print functionX().next()
print functionX().next()
print f1.next()
print f1.next()
