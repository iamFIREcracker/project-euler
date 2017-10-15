#!/usr/bin/python
# -*- coding: Latin-1 -*-
from __future__ import division
from math import hypot


def memoize(func):
  """Cache the results returned from the given function.
  """
  results = {}
  def wrapper(*args):
    try:
      return results[args]
    except KeyError:
      results[args] = value = func(*args) 
      return value
    except:
      return func(*args)
  return wrapper

def divisor(n):
  """Generate the list of the integer divisors of the given number.
  """
  for i in xrange(1, n // 2 + 1):
    if n % i == 0:
      yield i

def factor(n):
  """Generate the list of the factors of the given number.
  """
  yield 1
  i = 2
  limit = n ** 0.5
  while i <= limit:
    if not n % i:
      yield i
      n //= i
      limit = n ** .5
    else:
      i += 1
  if n > 1:
    yield n

def fibonacci(n):
  """Generate the list of the first n numbers of the Fibonacci serie.
  """
  a, b = 1, 1
  while n:
    yield b
    (a, b) = (b, a + b)
    n -= 1

"""Generate a list of digits from the Fibonacci serie: n is the upper bound
"""
def fibonacci1(n):
  a, b = 1, 1
  while b < n:
    yield b
    a, b = b, a + b

"""Generate the next lexicographic permutation of the given sequence
"""
def next_permutation(s):
  for i in reversed(xrange(len(s))):
    if s[i] > s[i-1]:
      break
  else:
    return []

  k = i
  for j in xrange(i, len(s)):
    if s[k] >= s[j] and s[j] > s[i-1]:
      k = j
  t = s[i-1]
  s[i-1] = s[k]
  s[k] = t
  s[i:] = s[len(s)-1:i-1:-1]
  return s

"""Check wether the given number is palindromic or not
"""
def palindromic(n):
  if type(n) != 'str':
    n = str(n)
  return n == n[::-1]

"""Generate a list of prime numbers: n is the upper bound
"""
def primes(n):
  if n >= 1:
    yield 2
    n -= 1
    primes = [2]
    i = 3
    while n:
      for p in primes:
        if not i%p or p*p > i:
          break
      if i%p:
        yield i
        primes.append(i)
        n -= 1
      i += 2

"""Generate a list of prime numbers: n is the upper bound
"""
def primes1(n):
  if n >= 2:
    yield 2
    primes = [2]
    for i in xrange(3, n, 2):
      for p in primes:
        if not i%p or p*p > i:
          break
      if i%p:
        yield i
        primes.append(i)

def isprime(n):
  """Check wether the given number is prime or not.
  """
  if n in [2, 3, 5, 7]:
    return True

  if n % 2 == 0:
    return False

  for i in xrange(3, int(n ** 0.5), 2):
    if n % i == 0:
      return False
  return True

"""Generate a list of the first k Pythagorean triplets
"""
def pythagorean_triplets(k, primitive=True):
  if k >= 1:
    m = 2
    while True:
      for n in xrange(1, m):
        if m%2 and n%2:
          continue
        a, b, c = n, m, hypot(n, m)
        if c != int(c):
          continue
        c = int(c)
        if primitive:
          fa, fb, fc = set(factor(a)), set(factor(b)), set(factor(c))
          if len(fa.intersection(fb.intersection(fc))) != 1:
            continue
        yield a, b, c
        k -= 1
        if not k:
          return
      m += 1

def triangle_sequence(n=1):
  """Generate the numbers from the Triangle number sequence starting from the
  given one, if specified.
  """
  while True:
    yield n * (n + 1) // 2
    n += 1

def pentagonal_sequence(n=1):
  """Generate the numbers from the Pentagonal number sequence starting from the
  given one, if specified.
  """
  while True:
    yield n * (3 * n - 1) // 2
    n += 1

def hexagonal_sequence(n=1):
  """Generate the numbers from the Hexagonal number sequence starting from the
  given one, if specified.
  """
  while True:
    yield n * (2 * n - 1)
    n += 1
