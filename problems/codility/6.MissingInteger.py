from typing import List
from itertools import combinations


"""
번역하기 복잡... 원문을 그대로 옮김
Write a function:
    def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
    Given A = [1, 2, 3], the function should return 4.
    Given A = [−1, −3], the function should return 1.
Write an efficient algorithm for the following assumptions:
"""


def solution(A):
    # current_min = 1
    # positive_count = 0
    # one_diff_count = 0
    #
    # A.sort()
    #
    # for i in range(len(A) - 1):
    #     if A[i+1] < 0 and A[i] < 0:
    #         next
    #     elif A[i+1] > 0 and A[i] < 0:
    #         current_min = A[i+1] - 1 if A[i+1] != 1 else 1
    #     elif A[i+1] > 0 and A[i] > 0:
    #         if positive_count == 0 and A[i] > 1:
    #             return 1
    #         else:
    #             positive_count += 1
    #
    #         if A[i+1] - A[i] > 1:
    #             return A[i] + 1
    #         else:
    #             one_diff_count += 1
    #
    # if positive_count == 0:
    #     return 1
    #
    # if positive_count == one_diff_count:
    #     current_min = A[-1] + 1
    #
    # return current_min

    current_min = 1
    A.sort()

    for e in A:
        if e == current_min:
            current_min += 1
        elif e >= current_min:
            break

    return current_min



if __name__ == "__main__":
    tests = [
        ([3, 4, 4, 6, 1, 4, 4], 2),
    ]

    for A, answer in tests:
        print(f"result: {solution(A)}, answer: {answer}")

