"""What is the total of all the name scores in the file?
"""
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

total = 0
for i, name in enumerate(sorted(raw_input().replace('"', '').split(','))):
  total += sum([alphabet.index(c) + 1 for c in name])*(i + 1)
print total
