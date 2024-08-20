# Problem 5: Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?
import math

def smallestMult(n):
    range_n = range(1, n+1)
    return math.lcm(*range_n)

# Euclidean algorithm
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# lcm(a, b) = a*b / gcd(a, b)

def test(n, answer):
    if smallestMult(n) == answer:
        print(f"test case {n} Passed")
    else:
        print(f"test case {n} Failed")

# Test cases
test(10, 2520)
test(13, 360360)
test(20, 232792560)