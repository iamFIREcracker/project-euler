"""Your task has been made easy, as the encryption key consists of three lower
case characters. Using cipher1.txt (right click and 'Save Link/Target As...'),
a file containing the encrypted ASCII codes, and the knowledge that the plain
text must contain common English words, decrypt the message and find the sum of
the ASCII values in the original text.
"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def ReadInts():
  return map(int, raw_input().strip().split(','))

def Password():
  for c1 in alphabet:
    for c2 in alphabet:
      for c3 in alphabet:
        yield (ord(c1), ord(c2), ord(c3))
  

message = ReadInts()
for p in Password():
  decrypted = ''.join(chr(p[i%3]^c) for i, c in enumerate(message))
  if ' the ' in decrypted or ' and ' in decrypted:
    print sum(ord(c) for c in decrypted)
    break
