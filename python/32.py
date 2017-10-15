"""Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.
"""
def IntToSeq(n):
  s = []
  while n:
    n, r = divmod(n, 10)
    s.append(r)
  return s

for d1 in range(4):
  for m1 in range(10**(d1 - 1), 
  for d2 in
