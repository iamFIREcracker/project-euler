"""What is the position of the cursor after 10 ** 12 steps in D50 ?
Give your answer in the form x,y with no spaces.
"""
# import re
# 
# evo = {'a': 'aRbFR', 'b': 'LFaLb'}
# regex = re.compile("(%s)" % "|".join(map(re.escape, evo.keys())))
# regex.sub(lambda mo: evo[mo.string[mo.start():mo.end()]], d)

def IsLeft(n):
  return (((n & -n) << 1) & n) != 0

def Pos(n, D):
  while True:
    if n < ((2 << D) - 1) >> 2:
      D -= 1
    else: break

  for i in xrange(1, D + 1):
    if i == 1: d = ['R']
    else:
      s = []
      for e in d:
        if e == 'R': s.insert(0, 'L')
        else: s.insert(0, 'R')
      d = d + d[0:1] + s

  (x, y) = (0, 1)
  (dx, dy) = (0, 1)
  for e in d[0:n]:
    if e == 'R': (dx, dy) = (dy, -dx)
    else: (dx, dy) = (-dy, dx)
    (x, y) = (x + dx, y + dy)
  return (x, y)


for i in xrange(16):
    print Pos(i, 50)
