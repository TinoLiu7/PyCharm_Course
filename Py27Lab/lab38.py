# encoding=UTF-8
import itertools

l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]
l3 = [u'甲', u'乙', u'丙']
result1 = itertools.chain(l1, l2, l3)
for item in result1:
    print item,
print
l4 = [1, 2, 3, 4, 5]
result2 = itertools.permutations(l4, 2)
print list(result2)
result3 = itertools.combinations(l4, 3)
print list(result3)
