
"""
in-place 알고리즘으로 list에 val이 아닌 값의 갯수를 카운트하고 val을 제거
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        len_nums = len(nums)
        counts = 0
        idx = 0

        while idx != len_nums:
            if nums[idx] == val:
                nums.pop(idx)
                len_nums = len(nums)
            else:
                counts += 1
                idx += 1

        return counts


if __name__ == "__main__":
    tests = [
        ([1,1,2], 2, 2),
        ([0,0,1,1,1,2,2,3,3,4], 1, 7),
    ]

    func = Solution()

    for nums, val, answer in tests:
        print(f"result: {func.removeElement(nums, val)}, answer: {answer}")

