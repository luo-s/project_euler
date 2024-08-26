# Problem 14: Longest Collatz sequence

# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under the given limit, produces the longest chain?
# Note: Once the chain starts the terms are allowed to go above limit.

def longest_collatz_sequence(n):
    ans, cnt = 0, 0
    for i in range(1, n + 1):
        if cnt_collatz_sequence(i) > cnt:
            cnt = cnt_collatz_sequence(i)
            ans = i
    return ans

# def cnt_collatz_sequence(n):
#     cnt = 0
#     while (n != 1):
#         if n % 2:
#             n = 3 * n + 1
#         else:
#             n = n / 2
#         cnt += 1
#     return cnt

# optimized: memoization approach
def cnt_collatz_sequence(n, cnt_collatz_seq = {1:1, 2:2}):
    # base case
    if n in cnt_collatz_seq:
        return cnt_collatz_seq[n]
    # recursive case
    if n % 2:
       next_n = 3 * n + 1
    else:
       next_n = n // 2
    cnt_collatz_seq[n] = 1 + cnt_collatz_sequence(next_n, cnt_collatz_seq)
    return cnt_collatz_seq[n]


