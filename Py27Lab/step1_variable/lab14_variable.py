x = 38
print hex(id(x))
x = 39
print  hex(id(x))


class Person(object):
    def __init__(self, age):
        self.age = age


john = Person(38)
print hex(id(john)), hex(id(john.age))
john.age = 39
print hex(id(john)), hex(id(john.age))
