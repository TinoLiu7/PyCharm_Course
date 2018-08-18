set1 = {'A', 'P', 'P', 'L', 'E'}
print set1
set2 = {'P', 'I', 'N', 'E', 'A', 'P', 'P', 'L', 'E'}
print set2
set3 = {'B', 'A', 'N', 'A', 'N', 'A'}
print set3
print set1 | set3
print set1 & set3
print set1 ^ set3
print (set1 & set3) | (set1 ^ set3)
print len(set2), len(set1|set3)
# for item in set3:
#     set1.add(item)
# print set1

print set1 < set3, set3 < set1
print set1 < set2, set2 < set1