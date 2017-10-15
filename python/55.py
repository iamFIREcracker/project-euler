"""How many Lychrel numbers are there below ten-thousand?
"""

from util import palindromic

MAX = 10000
ITERATIONS = 50

def lychrel(n):
  for i in xrange(ITERATIONS):
    n += int(str(n)[::-1])
    if palindromic(n):
      return False
  return True

found = 0
for i in xrange(1, MAX + 1):
  if lychrel(i):
    found += 1
print found
