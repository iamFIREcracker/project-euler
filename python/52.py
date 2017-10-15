"""Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""
def IntToSeq(n):
  s = []
  while n:
    n, r = divmod(n, 10)
    s.append(r)
  return s

for d in range(1, 10):
  for x in xrange(10**(d - 1), (10**d)//6):
    s = set(IntToSeq(x))
    for m in range(2, 7):
      ss = set(IntToSeq(x*m))
      if len(ss) != 6 or len(s&ss) != 6: break 
    else: break
  else: continue
  break
print x
