"""Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target
As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the
bottom right by only moving right and down.
"""

memo = {}
matrix = [map(int, raw_input().split(',')) for i in xrange(80)]
for i in xrange(80):
  for j in xrange(80):
    values = []
    if j:
      values.append(memo[i, j - 1])
    if i:
      values.append(memo[i - 1, j])

    if values:
      memo[i, j] = min(values) + matrix[i][j]
    else:
      memo[i, j] = matrix[i][j]
print memo[79, 79]
