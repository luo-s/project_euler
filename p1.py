# Problem 1: Multiples of 3 or 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below the provided parameter value number.

def multiples_of_3_and_5(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

def test(number, answer):
    if multiples_of_3_and_5(number) == answer:
        print(f"test case {number} Passed")
    else:
        print(f"test case {number} Failed")

# Test cases
test(10, 23)
test(49, 543)
test(1000, 233168)
test(8456, 16687353)
test(19564, 89301183)