"""Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2,
3, 4.  Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3,
4, 5, 6.  Peter and Colin roll their dice and compare totals: the highest total
wins. The result is a draw if the totals are equal.  What is the probability
that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven
decimal places in the form 0.abcdefg
"""
from itertools import product

def Roll(dice, faces):
  memo = {}
  for p in product(''.join(str(i) for i in xrange(1, faces + 1)), repeat=dice):
    s = sum(map(int, p)) 
    if s in memo: memo[s] += 1
    else: memo[s] = 1
  return memo

peter = Roll(9, 4)
colin = Roll(6, 6)

lp = 4**9
lc = 6**6
prob = 0.0
for p in sorted(peter.keys()):
  count = 0
  for c in sorted(colin.keys()):
    if p > c: count += colin[c]
    else: break
  prob += 1.0*peter[p]/lp*count/lc
print '%.7F' % prob
