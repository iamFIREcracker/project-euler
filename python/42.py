"""Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
"""
from util import triangle_sequence

ts = []
for t in triangle_sequence():
  if t > 26*20: break
  ts.append(t)

s = 0
for word in raw_input().strip().replace("\"", "").split(","):
  if sum(ord(c) - 96 for c in word.lower()) in ts:
    s += 1
print s

