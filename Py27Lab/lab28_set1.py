set1 = {'A', 'P', 'P', 'L', 'E'}
set2 = {'P', 'I', 'N', 'E', 'A', 'P', 'P', 'L', 'E'}
set3 = {'B', 'A', 'N', 'A', 'N', 'A'}
print set1, set2, set3
print 'B' in set1, "B" in set2, '''B''' in set3
print set1 | set2, set1 | set3
print set1 & set2, set1 & set3
print set1 ^ set2, set1 ^ set3
print set1 < set2, set2 < set1
print set1 < set3, set3 < set1
set1.add('X')
print set1
#set1.add(set2)
#set1.add(['a'])
set1.add(('a','A'))
print set1