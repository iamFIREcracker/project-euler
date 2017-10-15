"""Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
"""

from itertools import product

from util import memoize
from util import isprime


def istruncatable(n):
  old = 0
  v = 1
  while n:
    (n, r) = divmod(n, 10)
    old = r * v + old
    if (n and not isprime(n)) or (old and not isprime(old)):
      return False
    v *= 10
  return True


msd = [2, 3, 5, 7]
od = [1, 3, 7, 9]
lsd = [3, 7]

digits = 2
count = 0
s = 0
while count < 11:
  if digits > 2:
    args = [msd]
    [args.append(od) for _ in xrange(digits - 2)]
    args.append(lsd)
  else:
    args = [msd, lsd]
  for seq in product(*args):
    n = reduce(lambda v, x: v * 10 + x, seq)
    if istruncatable(n):
      s += n
      count += 1
      if count == 11:
        break
  digits += 1
print s
