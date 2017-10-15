"""Which starting number, under one million, produces the longest chain?
n is even: n -> n/2
n is odd : n -> 3*n + 1
"""

memo = {}
I, M = 0, 0
for i in xrange(2, 1000000):
  n = i
  seq = [n]
  while n != 1: 
    offset = 0
    if n in memo:
      seq.pop()
      offset = memo[n]
      break

    if n%2:
      n = 3*n + 1
    else:
      n = n/2
    seq.append(n)
  for k, n in enumerate(seq):
    memo[n] = len(seq) - k + offset
  if memo[i] > M:
    I, M = i, memo[i]
print I
