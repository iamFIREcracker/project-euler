"""Using network.txt (right click and 'Save Link/Target As...'), a 6K text file
containing a network with forty vertices, and given in matrix form, find the
maximum saving which can be achieved by removing redundant edges whilst
ensuring that the network remains connected.
"""
def Kruscal(T, S):
  W = 0
  while S:
    (w, i, j) = S.pop(0)

    if t[i] == t[j]: continue

    T[t[i]] += T[t[j]]

    old = t[j]
    for n in T[t[j]]:
      t[n] = t[i]
    T[old] = []

    W += w

  return W

N = 40
tot = 0
for i in xrange(N):
  for (j, w) in enumerate(raw_input().strip().split(',')):
    if i == 0 and j == 0: edges = []
    if w == '-': continue
    edges.append((int(w), i, j))
    tot += int(w)

T = [[i] for i in xrange(N)]
S = sorted(edges)

t = [i for i in xrange(N)]

print tot/2 - Kruscal(T, S)
