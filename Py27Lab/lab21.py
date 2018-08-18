x = 5
print 'when x=5, x in:', hex(id(x))
x = 6
print 'when x=6, x in:', hex(id(x))


class Person:
    def __init__(self, age):
        self.age = age
        pass

    pass


p1 = Person(5)
print "when p1.age=5, p1=%s, p1.age=%s" % (hex(id(p1)), hex(id(p1.age)))
p1.age = 6
print "when p1.age=6, p1=%s, p1.age=%s" % (hex(id(p1)), hex(id(p1.age)))
