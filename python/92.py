"""How many starting numbers below ten million will arrive at 89?
"""
from math import log
from math import ceil
from operator import mul

def Generate(alphabet, repeat, i=0, sequence=[]):
  for j in xrange(i, len(alphabet)):
    if repeat == 1: yield sequence + [alphabet[j]]
    else:
      for g in Generate(alphabet, repeat - 1, j, sequence + [alphabet[j]]):
        yield g

def IsHappy(n):
  if n > M or memo[n] == -1:
    s = 0
    while n:
      (n, r) = divmod(n, 10)
      s += square[r]
    n = s
    if n == 1: memo[n] = 1
    elif n == 89: memo[n] = 0
    else: memo[n] = IsHappy(n)
  return  memo[n]

N = 10000000
M = int(ceil(log(N, 10)))
memo = [-1 for _ in xrange(81*M + 1)]
square = map(lambda x: x*x, range(10))
f = [1] + [reduce(mul, range(1, i + 1)) for i in xrange(1, 10)]
count = 0
for d in xrange(1, M + 1):
  for s in Generate(range(1, 10), d):
    n = reduce(lambda x, y: x*10 + y, s)
    if n >= N: break
    if not IsHappy(n):
      l = [0 for _ in xrange(10)]
      l[0] = M - d
      for v in s:
        l[v] += 1
      count += f[M]/reduce(mul, map(lambda x: f[x], l))
print count
