"""What is the first value which can be written as the sum of primes in over
five thousand different ways?
"""
from util import primes1

coins = [p for p in primes1(100)]

memo = [[0] * len(coins)]
i = 0
while True:
  i += 1
  current = []
  for (j, c) in enumerate(coins):
    if c > i: current.append(0)
    elif c == i: current.append(1)
    else:
      s = sum(n for n in memo[i - c][j:])
      current.append(s)
  if sum(current) > 5000: break
  memo.append(current)
print i
