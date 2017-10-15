from util import triangle_sequence
from util import pentagonal_sequence
from util import hexagonal_sequence

triangle = triangle_sequence(285)
pentagonal = pentagonal_sequence(165)
hexagonal = hexagonal_sequence(143)

triangle.next()
t = triangle.next()
p = pentagonal.next()
h = hexagonal.next()
while True:
  while t < h:
    t = triangle.next()
  while p < t:
    p = pentagonal.next()
  while h < p:
    h = hexagonal.next()
  if t == p == h:
    break

print t
