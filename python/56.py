"""Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?
"""
m = 0
for a in xrange(1, 100):
  n = 1
  for b in xrange(1, 100):
    n *= a
    m = max(m, sum(map(int, list(str(n)))))
print m
