"""Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""
print sum([i**i for i in xrange(1, 1001)])%10000000000
