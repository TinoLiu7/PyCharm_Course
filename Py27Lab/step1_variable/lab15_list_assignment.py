list1 = ['a', 'b', 'c', 'd']
list2 = list1
list3 = list(list1)
list4 = list1[:]
print list1, list2, list3, list4
list1[0] = 'o'
list2[1] = 'O'
list1[2] = '0'
print list1, list2, list3, list4
