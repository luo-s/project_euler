# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.

# What is the nth prime number?

# # Python prime library https://pypi.org/project/primePy/ 
# from primePy import primes
# def nth_prime(n):
#     return primes.first(n)[-1]

import math
def nth_prime(n):
    count = 0
    p = 2
    while (count < n):
        if is_prime(p):
            count += 1
        p += 1
    return p-1

def is_prime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

# # Sieve of Eratosthenes
# def sieve_of_eratosthenes(limit):
#     primes = [True] * (limit + 1)
#     p = 2
#     while p * p <= limit:
#         if primes[p]:
#             for i in range(p * p, limit + 1, p):
#                 primes[i] = False
#         p += 1
#     return [p for p in range(2, limit + 1) if primes[p]]

