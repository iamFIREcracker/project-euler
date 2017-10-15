"""Find the least value of n for which p(n) is divisible by one million."""

n = 0
while True:
  n += 1
  coins = [i for i in xrange(1, n + 1)]
  memo = [[0] * len(coins)]
  i = 0
  while i < n:
    i += 1
    current = []
    for (j, c) in enumerate(coins):
      if c > i: current.append(0)
      elif c == i: current.append(1)
      else:
        s = sum(n for n in memo[i - c][j:])
        current.append(s%1000000)
    memo.append(current)
  s = sum(current)
  print n, s
  if s == 0: break
print n
