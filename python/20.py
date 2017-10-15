"""Find the sum of the digits in the number 100!
"""
import operator

print sum([int(c) for c in str(reduce(operator.mul,
                                      [i for i in xrange(1, 101)]))])
