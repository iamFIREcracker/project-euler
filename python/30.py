"""Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits
"""
def digits(n):
  s = []
  while n:
    (n, r) = divmod(n, 10)
    s.insert(0, r)
  return s

memo = [i**5 for i in xrange(10)]
print sum(i for i in xrange(10, 9**5*5)
              if i == sum(memo[d] for d in digits(i)))
