# lab31
import demoModule as d

print "my main lab31", d.foo(1, 2), d.bar(3, 4)

from demoModule import (foo, bar)

print "then, foo=", foo(5, 6), bar(7, 8)

from demoModule import foo as f, bar as g

print "finally, foo=", f(9, 10), g(11, 12)
