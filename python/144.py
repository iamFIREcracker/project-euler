"""How many times does the beam hit the internal surface of the white cell
before exiting?
"""

from math import sqrt


def normalize(x, y):
  s = sqrt(x ** 2 + y ** 2)
  return (x / s, y / s)

def direction(x1, y1, x2, y2):
  dx = 1
  dy = ((y2 - y1)/(x2 - x1))
  if x1 > x2:
    dx *= -1
  return normalize(dx, dy)

def reflex(x, y, dx, dy):
  try:
    (nx, ny) = normalize(1, abs(y / (4 * x)))
  except ZeroDivisionError:
    (nx,  ny) = (0, -1)
  if x > 0:
    nx *= -1
  if y > 0:
    ny *= -1

  dot = dx * nx + dy * ny
  (rx, ry) = (dx - 2 * nx * dot, dy - 2 * ny * dot)
  return (rx, ry)

def intersect(x, y, dx, dy):
  while True:
    m = dy / dx
    q = y - m * x

    (m2, q2) = (m**2, q**2)
    m2p4 = m2 + 4
    delta = sqrt(25 * m2 - q2 + 100)
    x1 = (2 * delta - m * q) / m2p4
    y1 = m * x1 + q
    if abs(x - x1) < 0.00001 and abs(y - y1) < 0.00001:
      x1 = (-2 * delta - m * q) / m2p4
      y1 = m * x1 + q
    (x, y) = (x1, y1)
    yield (x, y)

    (dx, dy) = reflex(x, y, dx, dy)


(x1, y1) = (0.0, 10.1)
(x2, y2) = (1.4, -9.6)
(dx, dy) = normalize(x2 - x1, y2 - y1)
c = 0
for (x, y) in intersect(x1, y1, dx, dy):
  if -0.01 <= x <= 0.01 and y > 0:
    break
  c += 1
print c
