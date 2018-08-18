def fib(max):
    prev, current = 0, 1
    counter = 0
    while counter < max:
        counter += 1
        yield current
        prev, current = current, current + prev
print(list(fib(10)))
print([i for i in fib(10)])
print(*[i for i in fib(10)])