class Foo(object):
    def __init__(self):
        self.counter = 0
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < 10:
            print("now, counter=%d" % self.counter)
            self.counter += 1
            return self.counter
        else:
            raise StopIteration()


foo1 = Foo()


def simple_variable_arguments(*args):
    for e in args:
        print("element inside args=%s" % (str(e)))
simple_variable_arguments(*foo1)
simple_variable_arguments(foo1)
foo2 = Foo()
simple_variable_arguments(*[element for element in foo2])