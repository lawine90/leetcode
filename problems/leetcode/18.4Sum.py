from typing import List
from itertools import product

"""
주어진 nums의 4개 element 조합이 target과 동일한 모든 조합을 찾아라
https://leetcode.com/problems/4sum/description/
e.g. nums = [1,0,-1,0,-2,2], target = 0 --> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        nums.sort()

        for left0 in range(len(nums) - 3):
            leaved = nums[left0+1:]
            for right0 in list(reversed(range(len(nums))))[:len(leaved)-2]:
                left1 = left0 + 1
                right1 = right0 - 1

                while left1 < right1:
                    current_comb = [nums[left0], nums[left1], nums[right1], nums[right0]]
                    current_sum = sum(current_comb)

                    if current_sum == target and current_comb not in results:
                        results.append(current_comb)

                    if current_sum < target:
                        left1 += 1
                    else:
                        right1 -= 1

        return results


if __name__ == "__main__":
    tests = [
        ([1,0,-1,0,-2,2], 0),
        ([2,2,2,2,2], 8),
    ]

    func = Solution()

    for nums, target in tests:
        print(f"result: {func.fourSum(nums, target)}")

