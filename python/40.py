"""If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
"""
targets = [1, 10, 100, 1000, 10000, 100000, 1000000]

d = 1
c = 0
bounds = []
while c <= targets[-1]:
  (l, r) = (c + 1, c + d*(10**d - 10**(d - 1)))
  bounds.append((l, r))
  c = r
  d += 1

p = 1
for t in targets:
  for (d, (l, r)) in enumerate(bounds):
    if t >= l and t <= r:
      t -= l
      (tn, td) = divmod(t, d + 1)
      p *= int(str(10**d + tn)[td])
print p
