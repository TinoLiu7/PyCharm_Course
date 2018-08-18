list1 = list('abcdefg')
list2 = list1
list3 = list1[:]
list4 = list(list1)
print "list1:%s, list2:%s" % (hex(id(list1)), hex(id(list2)))
print "list3:%s, list4:%s" % (hex(id(list3)), hex(id(list4)))
print list1, list2, list3, list4
list1[0] = '*'
list2[1] = 'o'
list1[2] = 'O'
list2[3] = '+'
print list1, list2, list3,list4
