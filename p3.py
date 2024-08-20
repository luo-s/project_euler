# Problem 3: Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the given number?

def largest_prime_factor(number):
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
    return number

def test(number, answer):
    if largest_prime_factor(number) == answer:
        print(f"test case {number} Passed")
    else:
        print(f"test case {number} Failed")

# Test cases
test(2, 2)
test(3, 3)
test(5, 5)
test(7, 7)
test(32, 2)
test(13195, 29)
test(600851475143, 6857)