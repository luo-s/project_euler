# Problem 5: Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?

# # lcm(a, b) * gcd(a, b) = a * b 

def smallestMult(n):
    # Euclidean algorithm
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    def lcm(a, b):
        return a * b / gcd(a, b)
    ans = 1
    for i in range(n):
        ans = lcm(ans, i + 1)
    return ans

# import math
# def smallestMult(n):
#     range_n = range(1, n+1)
#     return math.lcm(*range_n)
