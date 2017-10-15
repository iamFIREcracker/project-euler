"""Find the value of d  1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""


def recurring_cycle(d):
  n = 1
  cycle = {}
  while True:
    n *= 10
    (v, n) = divmod(n, d)
    if n in cycle:
      return len(cycle) - cycle[n]
    if n == 0:
      return 0
    else:
      cycle[n] = len(cycle)

(m, b) = (None, None)
for d in xrange(2, 1000):
  v = recurring_cycle(d)
  if m is None or v > m:
    (m, b) = (v, d)
print b
