def function1():
    result = 0
    for i in range(10):
        result += 1
        yield result
    pass
print(function1(), next(function1()),next(function1()))
f1 = function1()
print(next(f1),next(f1))
f2 = function1()
print ([i for i in f2])
f3 = function1()
print (list(f3))