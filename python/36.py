"""Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.
"""

from util import palindromic

def binary(n):
  r = ''
  while n > 0:
    r += str(n&1)
    n >>=  1
  return r[::-1]

print sum(i for i in xrange(1000000) if palindromic(i) and palindromic(binary(i)))
