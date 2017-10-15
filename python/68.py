"""Find the maximum total from top to bottom of the given triangle
"""

SIZE = 100
triangle = [map(int, raw_input().split()) for i in xrange(SIZE)]
memo = {(0, 0): triangle[0][0]}
M = memo[0, 0]
for i in xrange(1, SIZE):
  for j in xrange(i + 1):
    values = [0]
    if j:
      values.append(memo[i - 1, j - 1])
    if j != i:
      values.append(memo[i - 1, j])
    memo[i, j] = triangle[i][j] + max(values)
    M = max(M, memo[i, j])
print M
