"""How many different ways can one hundred be written as a sum of at least two
positive integers?
"""
MAX = 100
coins = xrange(1, MAX)

memo = [[0] * len(coins)]
for i in xrange(1, MAX + 1):
  current = []
  for (j, c) in enumerate(coins):
    if c > i: current.append(0)
    elif c == i: current.append(1)
    else:
      s = sum(n for n in memo[i - c][j:])
      current.append(s)
  memo.append(current)

print sum(memo[-1])
