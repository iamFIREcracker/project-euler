"""Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""
from util import primes

def IsPrime(n):
  for d in xrange(2, int(n**0.5) + 1):
    if n%d == 0: return False
  return True

MAX = 1000000
memo = []
(pp, pl) = (0, 0)
for p in primes(MAX):
  if p == 2:
    memo.append(p)
    continue
  i = 0
  while i < len(memo):
    memo[i] += p
    if memo[i] > MAX: break
    else:
      if IsPrime(memo[i]):
        if i > pl:
          pl = i
          pp = memo[i]
      i += 1
  else:
    memo.insert(0, p)
    continue
  break
print pp

