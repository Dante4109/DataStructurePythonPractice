# Task 1
# Task description

# This is a demo task.

# Write a function:

#     def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

#         N is an integer within the range [1..100,000];
#         each element of array A is an integer within the range [−1,000,000..1,000,000].

# Copyright 2009–2024 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    n = sorted(i for i in set(A) if i > 0)  # Remove duplicates and negative numbers
    if not n:
        return 1
    ln = len(n)

    for i in range(1, ln + 1):
        if i != n[i - 1]:
            return i

    return ln + 1


print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1, -3]))
