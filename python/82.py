"""Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target
As...'), a 31K text file containing a 80 by 80 matrix, from the left column to
the right column.
"""
from sys import maxint

def ReadInts():
  return map(int, raw_input().strip().split(','))

N = 80
matrix = [ReadInts() for _ in xrange(N)]
memo = [[matrix[i][0]] + [maxint for _ in xrange(N - 1)] for i in xrange(N)]
for j in xrange(N - 1):
  for i in xrange(N):
    s = memo[i][j] + matrix[i][j + 1]
    if s < memo[i][j + 1]:
      memo[i][j + 1] = s

      for k in xrange(i - 1, -1, -1):
        s += matrix[k][j + 1]
        if s < memo[k][j + 1]: memo[k][j + 1] = s
        else: break

      s = memo[i][j + 1]
      for k in xrange(i + 1, N):
        s += matrix[k][j + 1]
        if s < memo[k][j + 1]: memo[k][j + 1] = s
        else: break

print min(memo[i][j + 1] for i in xrange(N))
