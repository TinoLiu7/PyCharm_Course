import decimal as d

a1 = 1.5
a2 = 2.5
d1 = d.Decimal(a1)
d2 = d.Decimal(a2)
print(a1, a2, d1, d2)
print("up", d.Decimal(d1.quantize(d.Decimal('1')
                                  , rounding=d.ROUND_HALF_UP)))
print("up", d.Decimal(d2.quantize(d.Decimal('1')
                                  , rounding=d.ROUND_HALF_UP)))
print("down", d.Decimal(d1.quantize(d.Decimal('1')
                                    , rounding=d.ROUND_HALF_DOWN)))
print("down", d.Decimal(d2.quantize(d.Decimal('1')
                                    , rounding=d.ROUND_HALF_DOWN)))
print(d.Decimal(d1.quantize(d.Decimal('1')
                            , rounding=d.ROUND_HALF_EVEN)))
print(d.Decimal(d2.quantize(d.Decimal('1')
                            , rounding=d.ROUND_HALF_EVEN)))
