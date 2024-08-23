# Problem 9: Special Pythagorean triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# There exists exactly one Pythagorean triplet for which a + b + c = 1000. 
# Find the product abc such that a + b + c = n.

def specialPythagoreanTriplet(n):
    ans = set()
    for a in range(1, n // 2 + 1):
        for b in range(a, n // 2 + 1):
            for c in range(b, n // 2 + 1):
                if pow(a, 2) + pow(b, 2) == pow(c, 2) and a + b + c == n:
                    ans.add(a * b * c)
    return ans
                
def test(n, answer):
    if specialPythagoreanTriplet(n) == answer:
        print(f"test case {n} Passed")
    else:
        print(f"test case {n} Failed")

test(24, {480})
test(120, {49920, 55080, 60000})
test(1000, {31875000})