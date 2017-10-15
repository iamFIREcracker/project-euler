"""By solving all fifty puzzles find the sum of the 3-digit numbers found in
the top left corner of each solution grid; for example, 483 is the 3-digit
number found in the top left corner of the solution grid above
"""
from heapq import heappush, heappop

BOX = 3
SIZE = BOX*BOX

def Cross(a, b):
  for i in a:
    for j in b:
      yield (i, j)

def Box(i, j):
  (ii, jj) = (i//BOX*BOX, j//BOX*BOX)
  for (iii, jjj) in Cross(xrange(ii, ii + BOX), xrange(jj, jj + BOX)):
    yield (iii, jjj)

def Options(sudoku, i, j):
  o = set(range(1, SIZE + 1))
  o -= set([sudoku[i][k] for k in xrange(SIZE)])
  o -= set([sudoku[k][j] for k in xrange(SIZE)])
  o -= set([sudoku[k][l] for (k, l) in Box(i, j)])
  return o

def Heuristic(sudoku):
  heap = []
  for (i, j) in Cross(xrange(SIZE), xrange(SIZE)):
    if not sudoku[i][j]:
      o = Options(sudoku, i, j)
      heappush(heap, (len(o), o, i, j))
  while heap:
    yield heappop(heap)

def Solve(sudoku):
  for (l, o, i, j) in Heuristic(sudoku):
    for v in o:
      sudoku[i][j] = v
      if Solve(sudoku): return True
      sudoku[i][j] = 0
    return False
  return True

s = 0
N = 50
for case in xrange(N):
  raw_input()
  sudoku = [[int(c) for c in raw_input().strip()] for _ in xrange(SIZE)]
  Solve(sudoku)
  s += sudoku[0][0]*100 + sudoku[0][1]*10 + sudoku[0][2]
print s
