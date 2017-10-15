"""What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
5, 6, 7, 8 and 9?
"""
from operator import mul
from util import next_permutation

N = 1000000

s = range(10)
for (i, n) in enumerate(range(9, 1, -1)):
  f = reduce(mul, range(1, n + 1))
  j = i
  while N > f:
    N -= f
    j += 1
  s = s[:i] + s[j:j + 1] + s[i:j] + s[j + 1:]

while N != 1:
  s = [s[0]] + next_permutation(s[1:])
  N -= 1
print ''.join(map(str, s))
