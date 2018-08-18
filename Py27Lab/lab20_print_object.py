class Foo(object):
    def __str__(self):
        return "Foo:string formatter"

    def __repr__(self):
        return "Foo:repr formatter"

    pass


f1 = Foo()
print "%s,%r" % (f1, f1)
print "{0!s},{0!r}".format(f1)
print (f1,)
print (f1)
print [f1]
print {f1}
print {'k1': f1}
