"""How many circular primes are there below one million?
"""
from itertools import product

def IsPrime(n):
  for d in xrange(2, int(n**0.5) + 1):
    if n%d == 0: return False
  return True

s = 4 # 2, 3, 5, 7
l = 2
while l < 7:
  for p in product([1, 3, 7, 9], repeat=l):
    p  = list(p)
    for _ in range(l):
      if not IsPrime(reduce(lambda x, y: x*10 + y, p)): break
      p = p[1:] + p[0:1]
    else:
      s += 1
  l += 1
print s
