class Foo(object):
    def __str__(self):
        return "Foo:string 格式化的結果"

    def __repr__(self):
        return "Foo:repr 格式化的結果"

    pass


f1 = Foo()
print("%s, %r" % (f1, f1))
print("{0!s},{0!r},{0!a}".format(f1))
