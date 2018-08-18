# encoding=UTF-8
u1  = u'中文輸入法'
print u1.encode('utf8')
print 'repr format:', repr(u1.encode('utf8'))
print 'repr format2:', repr(u1.encode('ms950'))
print 'repr format3:', repr(u1.encode('big5'))

encoded_string1 = '\xe5\xad\x97'
print repr(encoded_string1), encoded_string1
convert_latin = encoded_string1.decode('latin-1')
print repr(convert_latin), convert_latin
convert_utf8 = encoded_string1.decode('utf-8')
print repr(convert_utf8), convert_utf8