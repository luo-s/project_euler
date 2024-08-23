# Problem 10: Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below n.

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
        
def test(n, answer):
    if primeSum(n) == answer:
        print(f"test case {n} Passed")
    else:
        print(f"test case {n} Failed")

test(17, 41)
test(2001, 277050)
test(140759, 873608362)
test(2000000, 142913828922)