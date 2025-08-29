from typing import List
from itertools import combinations


"""
입력된 list of int를 K회 회전시켜라
rotation: list의 마지막 element를 맨 앞으로 가져와서 붙이기
"""
def solution(A, K):
    if len(A) == 0:
        return []

    for i in range(K):
        A = [A[-1]] + A[:len(A)-1]
    return A


if __name__ == "__main__":
    tests = [
        ([3, 8, 9, 7, 6], 3, [9, 7, 6, 3, 8]),
        ([1, 2, 3, 4], 4, [1, 2, 3, 4]),
    ]

    for nums, K, answer in tests:
        print(f"result: {solution(nums, K)}, answer: {answer}")

