from typing import List
from itertools import combinations


"""
주어진 nums에서 세 숫자의 합이 소수가 되는 경우의 수
"""
from math import sqrt
from itertools import combinations


def is_prime(x: int) -> bool:
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(nums):
    return sum(
        is_prime(sum(t))
        for t in combinations(nums, 3)
    )


if __name__ == "__main__":
    tests = [
        ([1,2,3,4], 1),
        ([1,2,7,6,4], 4),
    ]

    for nums, answer in tests:
        print(f"result: {solution(nums)}, answer: {answer}")

