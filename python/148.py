"""Find the number of entries which are not divisible by 7 in the first one
billion (109) rows of Pascal's triangle
"""
MAX = 10e9

def Tot(n):
  result = 0
  while n:
    result += n
    n -= 1
  return result

print Tot(MAX)
