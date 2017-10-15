"""How many, not necessarily distinct, values of  nCr, for 1  n  100, are greater than one-million?
"""
i = 0
n = 100
C = [[1]]
for N in xrange(1, n + 1):
  C.append([])
  for R in xrange(N):
    if not R: v = C[N - 1][R]
    else: v = C[N - 1][R - 1] + C[N - 1][R]
    C[N].append(v)
    if v > 1000000: i += 1
  C[N].append(1)
print i
