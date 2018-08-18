list1 = list('abc')
list2 = list('123')
list1.append(list2)
list1.append('k')
list1.append('PQRST')
print list1
list3 = list('abc')
list4 = list('123')
list3.extend(list4)
print list3
list5 = list('abc')
list6 = list('123')
list5 += list6
print list5
