# demoModule.py
def foo(a, b):
    return "[demoModule]foo:result=%d, aka %s" % ((a + b), str(a + b))


def bar(a, b):
    return "[demoModule]bar:result=%d, aka %s" % ((a * b), str(a * b))

if __name__ == '__main__':
    print foo(2, 3)
    print bar(4, 5)

    l1 = [1, 2, 3, '1', 'hello', 567.8, True, False, None]
    for element in l1:
        print "the element inside=%s" % str(element)
