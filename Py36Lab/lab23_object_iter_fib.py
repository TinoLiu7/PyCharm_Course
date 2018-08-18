class Fib(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.n < self.max:
            result = self.b
            self.a, self.b = self.b, self.a+self.b
            self.n += 1
            return result
        raise StopIteration()
print(list(Fib(10)))
for i in Fib(8):
    print('element=',i)