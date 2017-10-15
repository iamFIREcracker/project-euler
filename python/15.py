H, W = 21, 21

memo = {}
for i in reversed(xrange(H)):
  for j in reversed(xrange(W)):
    if i == H -1 and j == W - 1:
      memo[i, j] = 1
    elif i == H - 1:
      memo[i, j] = memo[i, j + 1]
    elif j == W - 1:
      memo[i, j] = memo[i + 1, j]
    else:
      memo[i, j] = memo[i, j + 1] + memo[i + 1, j]
print memo[0, 0]
