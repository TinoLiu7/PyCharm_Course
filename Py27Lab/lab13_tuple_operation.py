v1 = 5
v2 = 3
print 'step1', v1, v2
temp = v1
v1 = v2
v2 = temp
print 'step2', v1, v2
v3 = 6
v4 = 2
v3, v4 = v4, v3
print 'step3, after swap', v3, v4
v5 = 2.958
v6 = 'hello world'
print 'step4', v5, v6
v5, v6 = v6, v5
print 'step5', v5, v6
a1 = "spring"
a2 = "summer"
a3 = "autumn"
a4 = "winter"
a1, a2, a3, a4 = a3, a1, a4, a2
print 'result=', a1, a2, a3, a4
