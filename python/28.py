"""What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?
"""

def spiral(n):
  max = n**2
  yield 1
  i = 3
  inc = 2
  while i <= max:
    for k in xrange(3):
      yield i
      i += inc
    yield i
    inc += 2
    i += inc

print sum([n for n in spiral(1001)])
