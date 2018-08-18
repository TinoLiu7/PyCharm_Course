class Foo(object):
    def __str__(self):
        return '[Foo]:string format'
    def __repr__(self):
        return '[Foo]:repr format'
foo1 = Foo()

print 'print foo1 in str:%s, repr:%r'%(foo1, foo1)
print 'print foo1 in str:{0!s}, repr:{0!r}'.format(foo1)