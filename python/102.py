"""Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text
file containing the co-ordinates of one thousand "random" triangles, find the
number of triangles for which the interior contains the origin.
"""
def ReadPoints():
  l = list(map(int, raw_input().strip().split(",")))
  p = []
  for i in range(0, len(l), 2):
    p.append((l[i], l[i + 1]))
  return p

def CrossProduct(v1, v2):
  if v1[0]*v2[1] - v1[1]*v2[0] > 0: return True
  else: return False

def Sub(v1, v2):
  return (v1[0] - v2[0], v1[1] - v2[1])

def Neg(v1):
  return (-v1[0], -v1[1])

N = 1000
c = 0
O = (0, 0)
for _ in xrange(N):
  p = ReadPoints()
  for i in range(len(p)):
    (j, k) = ((i + 1)%len(p), (i + 2)%len(p))
    cr1 = CrossProduct(Sub(p[j], p[i]), Sub(p[k], p[i]))
    cr2 = CrossProduct(Sub(p[j], p[i]), Neg(p[i]))
    if cr1 ^ cr2: break
  else: c += 1
print c
