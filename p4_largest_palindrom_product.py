# Problem 4: Largest palindrome product

# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two n-digit numbers.


def largestPalindromeProduct(n):
    ans = 0
    for i in range(10**n - 1, 10**(n-1) - 1, -1):
        for j in range(10**n - 1, 10**(n-1) - 1, -1):
            if is_palindrome(i*j):
                ans = max(ans, i*j)
    return ans

# def is_palindrome(n):
#     return str(n) == str(n)[::-1]

def is_palindrome(n):
    string = str(n)
    l, r = 0, len(string) - 1
    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True

def test(n, answer):
    if largestPalindromeProduct(n) == answer:
        print(f"test case {n} Passed")
    else:
        print(f"test case {n} Failed")

# Test cases
test(2, 9009)
test(3, 906609)