# Problem 6: Sum square difference

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and 
# the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first n natural numbers and the square of the sum.

def sumSquareDifference(n):
    sum_of_squares = sum([pow(i, 2) for i in range(1, n + 1)])
    square_of_sum = pow(sum(range(1, n + 1)), 2)
    return square_of_sum - sum_of_squares

# def sumSquareDifference(n):
#     return pow((n * (n + 1) / 2), 2) - n * (n + 1) * (2 * n + 1) / 6

def test(n, answer):
    if sumSquareDifference(n) == answer:
        print(f"test case {n} Passed")
    else:
        print(f"test case {n} Failed")

# Test cases
test(10, 2640)
test(20, 41230)
test(100, 25164150)
