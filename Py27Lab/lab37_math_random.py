import math
import random

print math.pi, math.log10(10), math.log10(2)
print math.sqrt(5)
for i in range(100):
    print random.randint(1, 10),
l1 = ['apple', 'banana', 'citron', 'orange', 'watermelon']
for i in range(10):
    print random.choice(l1)
random.shuffle(l1)
print l1
