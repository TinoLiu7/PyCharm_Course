def someFunction():
    x = 100
    y = 200
    z = 300
    y = yield x
    yield y + z

f1 = someFunction()
print f1.next()
print f1.send(400)