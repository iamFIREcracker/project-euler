"""What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n  1?
"""
def IntToSeq(n):
  s = []
  while n:
    n, r = divmod(n, 10)
    s.insert(0, r)
  return s

def SeqToInt(s):
  n = 0
  while s:
    n = n*10 + s.pop(0)
  return n

for i in reversed(xrange(192, 10000)):
  s = IntToSeq(i)
  n = 2
  found = False
  while not found:
    s += IntToSeq(i*n)
    if len(s) > 9 or 0 in s: break
    if len(set(s)) == 9:
      found = True
    n += 1
  else: break
print SeqToInt(s)
