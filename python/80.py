"""For the first one hundred natural numbers, find the total of the digital
sums of the first one hundred decimal digits for all the irrational square
roots.
"""
from decimal import *

setcontext(Context(prec=1000))

total = 0
for i in xrange(1, 101):
  number = str(Decimal(i).sqrt()).replace('.', '')
  l = min(100, len(number))
  if i == 2:
    print sum([int(c) for c in number[:l]])
  total += sum([int(c) for c in number[:l]])
print total
