"""What is the 10001st prime number?
"""
from util import primes

print [p for p in primes(10001)][-1]
