"""What is the largest n-digit pandigital prime that exists?
"""
from itertools import permutations

def IsPrime(n):
  for d in xrange(2, int(n**0.5) + 1):
    if n%d == 0: return False
  return True

# 1 + 2 ... + 9 = 45 / 3 = 15
# 1 + 2 ... + 8 = 36 / 3 = 12
# 1 + 2 ... + 7 = 28 !!!
d = 7
pandig = [p for p in permutations(range(1, d + 1))]
for p in reversed(pandig):
  n = reduce(lambda x, y: x*10 + y, p)
  if IsPrime(n):
    print n
    break
