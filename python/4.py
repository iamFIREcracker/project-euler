"""Find the largest palindrome made from the product of two 3-digit numbers.
"""
from util import palindromic

max = 0
for a in xrange(999, 100, -1):
  for b in xrange(a, 100, -1):
    n = a*b
    if n <= max: break
    if palindromic(n):
      max = n
      break
  if b == a: break
print max
