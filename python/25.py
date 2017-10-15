"""What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

from util import fibonacci

for i, n in enumerate(fibonacci(10000)):
  if len(str(n)) == 1000:
    # +1 -> first two terms returned by our function are 1, 2 and not 1, 1
    # +1 -> i goes from 0 up to ...
    print i + 2
    break
