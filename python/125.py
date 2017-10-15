"""Find the sum of all the numbers less than 10**8 that are both palindromic and
can be written as the sum of consecutive squares.
"""
from util import palindromic

MAX = 100000000
memo = []
s = set()
for n in xrange(1, int(MAX**0.5)):
  n *= n
  i = 0
  while i < len(memo):
    memo[i] += n
    if memo[i] >= MAX: memo.pop(i)
    else:
      if palindromic(memo[i]):
        s.add(memo[i])
      i += 1
  memo.insert(0, n)
print sum(s)
