from typing import List
from itertools import combinations


"""
integer list인 nums에서 두 숫자의 합이 target과 일치하는 조합의 인덱스 찾아내기
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [
            [e1[0], e2[0]]
            for e1, e2 in combinations(enumerate(nums), 2)
            if e1[1] + e2[1] == target
        ][0]


if __name__ == "__main__":
    tests = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]

    s = Solution()

    for nums, target, answer in tests:
        print(f"result: {s.twoSum(nums, target)}, answer: {answer}")

