# encoding=UTF-8
import itertools

a1 = list('abc')
a2 = list('12345')
a3 = list(u'甲乙丙丁')
result1 = itertools.chain(a1, a2, a3)
for item in result1:
    print item,
print '---'

a4 = list('abcde')
result2 = itertools.permutations(a4, 2)
list2 = [item for item in result2]
for item in list2:
    print item,
print '---total=', len(list2)
result3 = itertools.combinations(a4, 3)
list3 = [item for item in result3]
for item in list3:
    print item,
print '--total=', len(list3)