string1 = "abcde12345"
string2 = string1*5
list1 = list(string2)
print type(string2), type(list1)
list1[0]='*'
list1[1]='.'
print list1[:10]
# abcde==> !
list1[:5]='!'
print list1[:10]
del list1[:6]
# 50 - 4 - 6 = 40
print list1[:10],len(list1)