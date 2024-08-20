# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.

# What is the nth prime number?
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
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return False
    return True

# Sieve of Eratosthenes
# def sieve_of_eratosthenes(limit):
#     primes = [True] * (limit + 1)
#     p = 2
#     while p * p <= limit:
#         if primes[p]:
#             for i in range(p * p, limit + 1, p):
#                 primes[i] = False
#         p += 1
#     return [p for p in range(2, limit + 1) if primes[p]]


def test(n, answer):
    if nth_prime(n) == answer:
        print(f"test case {n} Passed")
    else:
        print(f"test case {n} Failed")

# Test cases
test(6, 13)
test(10, 29)
test(100, 541)
test(1000, 7919)
test(10001, 104743)
