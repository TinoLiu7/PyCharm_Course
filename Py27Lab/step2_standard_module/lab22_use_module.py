import demoModule

print"inside lab22"
demoModule.plus(5, 6)

import demoModule as d

d.plus(7, 8)
d.multiply(9, 10)

from demoModule import plus, multiply

plus(11, 12)
multiply(13, 14)

from demoModule import plus as p
from demoModule import multiply as m

p(15, 16)
m(17, 18)
