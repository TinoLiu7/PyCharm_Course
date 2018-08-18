from decimal import Decimal as Dec
print Dec(3.14159)
print Dec('3.14159')
print Dec(314159)*Dec(0.00001)-Dec(3.14159)
print Dec(314159)*Dec('0.00001')-Dec('3.14159')