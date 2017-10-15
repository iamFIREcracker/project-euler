"""What is the value of the first triangle number to have over five hundred
divisors?
"""
from operator import mul

from util import factor, triangle_sequence


for n in triangle_sequence():
  old = 1
  m = 0
  div = []
  for f in factor(n):
    if f != old:
      div.append(m)
      m = 1
    else: m += 1
    old = f
  if div and reduce(mul, map(lambda n: n + 1, div)) - 1 > 500:
    print n
    break
