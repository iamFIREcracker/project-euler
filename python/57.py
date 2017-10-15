"""In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
"""
from fractions import Fraction
from math import floor
from math import log10


def root2():
  (n, d) = (1, 1)
  while True:
    (n, d) = (n + d + d, n + d)
    yield (n, d)


count = 0
root2 = root2()
for i in xrange(1000):
  (n, d) = root2.next()
  if floor(log10(n)) > floor(log10(d)):
    count += 1
print count
