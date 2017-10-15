"""Find the sum of all the multiples of 3 or 5 below 1000.
"""
print sum(x for x in xrange(1000) if not x%3 or not x%5)
