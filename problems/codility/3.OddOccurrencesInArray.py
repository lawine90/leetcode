from typing import List
from itertools import combinations


"""
입력된 리스트에서 페어가 되지 않는 요소를 찾아서 리턴하라
e.g. A = [9, 3, 9, 3, 9, 7, 9]
"""
def solution(A):
    # 아래 해결책은 A.count(e) 로 인해 연산 비용이 너무 높음.
    # a_set = set(A)
    #
    # for e in a_set:
    #     if A.count(e) % 2 != 0:
    #         return e
    #
    # return None

    from collections import Counter

    e_counts = Counter(A)
    for e, n in e_counts.items():
        if n % 2 != 0:
            return e

    return None


if __name__ == "__main__":
    tests = [
        ([9, 3, 9, 3, 9, 7, 9], 7),
    ]

    for nums, answer in tests:
        print(f"result: {solution(nums)}, answer: {answer}")

