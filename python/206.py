"""Find the unique positive integer whose square has the form
1_2_3_4_5_6_7_8_9_0, where each "_" is a single digit.
"""
lb = 1010101010 # 1020304050607080900**0.5
ub = 1389026623 # 1929394959697989990**0.5

last30 = True
n = 1010101030
while n < ub:
  if str(n*n)[::2] == "1234567890":
    print n
    break
  if last30: n += 40
  else: n += 60
  last30 = not last30
