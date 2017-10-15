"""There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from util import factor, pythagorean_triplets, hypot

for a, b, c in pythagorean_triplets(500, False):
  if a + b + c == 1000:
    print a*b*c
    break
