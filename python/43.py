"""Find the sum of all 0 to 9 pandigital numbers with this property.
"""
def Int2List(n, fill=3):
  l = []
  while n:
    n, r = divmod(n, 10)
    l.insert(0, r)
  l = [0]*(fill - len(l)) + l
  return l

def List2Int(l):
  s = 0
  for e in l:
    s = s*10 + e
  return s

s = map(Int2List, [i for i in range(17, 1000, 17)])
for d in [13, 11, 7, 5, 3, 2, 1]:
  t = []
  for e in s:
    n = List2Int(e[:2])
    for i in range(0, 1000, 100):
      m = n + i
      if m%d == 0:
        ee = [i/100] + e
        if len(ee) == len(set(ee)):
          t.append(ee)
  s = t
print sum(List2Int(n) for n in s)
