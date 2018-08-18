import decimal as d

d1 = d.Decimal(5 / 3.0)
print d.Decimal(d1.quantize(d.Decimal('.0001'),rounding=d.ROUND_HALF_UP))
print d.Decimal(d1.quantize(d.Decimal('.01'),rounding=d.ROUND_HALF_UP))
print d.Decimal(d1.quantize(d.Decimal('1'),rounding=d.ROUND_HALF_UP))
