"""Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.
"""
from math import log

def ReadInts():
  return list(map(int, raw_input().strip().split(",")))

N = 1000
for i in xrange(N):
  (b, e) = ReadInts()
  v = e*log(b)
  if not i or v > m:
    m = v
    j = i
print j + 1
