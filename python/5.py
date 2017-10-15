"""What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""
from util import factor

MAX = 20

memo = [[0 for _ in xrange(MAX)] for _ in xrange(MAX)]
for i in xrange(1, MAX + 1):
  for p in factor(i):
    memo[i - 1][p - 1] += 1

result = 1
for j in xrange(MAX):
  m = 0
  for i in xrange(MAX):
    m = max(m, memo[i][j])
  if m != 0: result *= (j + 1)**m
print result



