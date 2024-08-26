# Problem 10: Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below n.

# # Python prime library https://pypi.org/project/primePy/ 
# # primePy took unusual time for large n, it probably doens't apply Sieve of Eratosthenes Algorithm 
# from primePy import primes
# def primeSum(n):
#     return sum(primes.upto(n - 1))

def primeSum(n):
    # Sieve of Eratosthenes
    primes = [True] * (n + 1)
    p, ans = 2, 0
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    for i in range(2, n):
        if primes[i]:
            ans += i
    return ans
        