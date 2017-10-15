"""Find the sum of all numbers which are equal to the sum of the factorial of their digits.
"""
from operator import mul

fact = [1] + [reduce(mul, xrange(1, i + 1)) for i in xrange(1, 10)]
print sum(i for i in xrange(10, fact[9]*7)
              if i == sum(fact[int(d)] for d in str(i)))
