"""Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target
As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the
bottom right by moving left, right, up, and down.
"""
from heapq import heappush, heappop
from sys import maxint

def ReadInts():
  return list(map(int, raw_input().strip().split(",")))

def Neighbors(i, j, h, w):
  if i != 0: yield (i - 1, j)
  if j != w - 1: yield (i, j + 1)
  if i != h - 1: yield (i + 1, j)
  if j != 0: yield (i, j - 1)

N = 80
matrix = [ReadInts() for _ in xrange(N)]

g = [[maxint for _ in xrange(N)] for _ in xrange(N)]
h = [[(N  - 1 - i) + (N - 1 - j) for j in xrange(N)] for i in xrange(N)] 

g[0][0] = 0
open = [(g[0][0] + h[0][0], 0, 0)]
close = [[maxint for _ in xrange(N)] for _ in xrange(N)]
while open:
  (f, i, j) = heappop(open)
  if (i, j) == (N - 1, N - 1):
    print g[i][j] + matrix[i][j]
    break
  for (ni, nj) in Neighbors(i, j, N, N):
    ng = g[i][j] + matrix[i][j]
    if ng < g[ni][nj]:
      g[ni][nj] = ng
      nf = ng + h[i][j]
      close[ni][nj] = nf
      heappush(open, (nf, ni, nj))
  close[i][j] = f
