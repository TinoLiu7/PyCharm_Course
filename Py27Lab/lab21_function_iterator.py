def function1():
    result = 0
    for i in range(10):
        result += 1
        yield result
    pass
print function1(), function1().next(), function1().next()
f1 = function1()
print f1.next(), f1.next()
f2 = function1()
print [i for i in f2]