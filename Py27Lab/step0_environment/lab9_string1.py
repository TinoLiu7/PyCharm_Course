string1 = "abcdefg1234567"
print string1[0], string1[13], string1[4]
# 3rd, 8th (not include)
print string1[2:7]
# print all
print string1[:]
# cut from 6th (second part)
print string1[:5], string1[5:]
# string index out of range
#print string1[14]
print string1[-1], string1[-14]
print string1[-5:]
# print 5th to N-1
print len(string1), string1[4:len(string1)-1]
string2 = 'www.uuu.com.tw'
print type(string2.split('.'))
return1 = string2.split('.')
print return1
print "*".join(return1)
string3 = 'xyz890'
return2 = list(string3)
print type(return2), return2
#part3
print 'www' in string2, 'Ww.' in string2, 'XYZ' not in string1
print string2+string3, string3*5, 5*string3
# from first to 10th(not include), each2
print string1[0:9:2]
print min(string1), max(string2), len(string3)

# part4
print string1.index('a'), string1.index('g'), string1.index('4')
#print string1.index(4)
#print string1.index('X')
print string2.count('w'), string2.count('.')