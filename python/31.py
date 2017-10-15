"""How many different ways can $2 be made using any number of coins?
"""
MAX = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]

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
