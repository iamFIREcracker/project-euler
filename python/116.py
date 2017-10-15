"""How many different ways can the black tiles in a row measuring fifty units
in length be replaced if colours cannot be mixed and at least one coloured tile
must be used?
"""

def memoize(func):
  results = {}
  def wrapper(*args):
    if args not in results:
      results[args] = func(*args)
    return results[args]
  return wrapper

@memoize
def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * factorial(n - 1)

def solve(n, step):
  s = 0
  for (i, j) in enumerate(xrange(n, -1, -step)):
    if not i: continue
    s += factorial(i + j) / (factorial(i) * factorial(j))
  return s

print solve(50, 2) + solve(50, 3) + solve(50, 4)
