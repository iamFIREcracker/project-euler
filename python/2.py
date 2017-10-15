"""Find the sum of all the even-valued terms in the sequence which do not
exceed four million.
"""
sum = 0
a, b = 1, 2
while True:
  if b >= 4000000:
    break
  if not b%2:
    sum += b
  a, b = b, a + b
print sum
