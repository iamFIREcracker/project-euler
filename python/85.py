"""Although there exists no rectangular grid that contains exactly two million
rectangles, find the area of the grid with the nearest solution.
"""
target = 2000000
min = 0
for n in range(2, 101):
  for m in range(n, 101):
    # triangle(n)*triangle(m)
    s = n*(n + 1)*m*(m + 1)/4

    if s > target: d = s - target
    else: d = target - s

    if not min or d < min: (a, b, min) = (n, m, d)
print a*b
