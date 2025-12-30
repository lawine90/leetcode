
"""
in-place 알고리즘으로 list에 들어있는 unique한 element의 수를 카운트하고 nums에 unique한 element만 남기는 함수 생성
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_nums = len(nums)

        idx = 1
        counts = 1

        while idx != len_nums:
            if nums[idx] == nums[idx - 1]:
                nums.pop(idx)
                len_nums = len(nums)
            else:
                counts += 1
                idx += 1

        return counts


if __name__ == "__main__":
    tests = [
        ([1,1,2], 2),
        ([0,0,1,1,1,2,2,3,3,4], 5),
    ]

    func = Solution()

    for s, answer in tests:
        print(f"result: {func.removeDuplicates(s)}, answer: {answer}")

