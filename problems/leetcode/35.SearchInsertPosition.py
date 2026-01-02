from typing import List

"""
# https://leetcode.com/problems/search-insert-position/description/
binary search로 target이 들어갈 위치
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if target > nums[-1]:
            return right + 1

        if target < nums[0]:
            return 0

        while left <= right:
            mid = (left + right) // 2
            #current_val = nums[mid]

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                return mid

            # if prev_val is not None:
            #     if nums[mid] < target < prev_val:
            #         print("!")
            #         mid = left + 1
            #         break
            #     elif prev_val < target < nums[mid]:
            #         print("!")
            #         mid = right
            #         break

            # prev_val = nums[mid]

        # 중요한 포인트: while이 끝나는 조건은 left 값이 right 값보다 커질 때.
        #   nums에 target이 없을 경우 while이 끝까지 도는데 이 때 left의 위치가 target이 들어가야 할 자리임
        #   e.g. nums = [1,3,5,6]; target = 7
        #       while1: mid = (0 + 3) // 2 = 1
        #               left = 2 (mid + 1)
        #               right = 3
        #       while2: mid = (2 + 3) // 2 = 2
        #               left = 3 (mid + 1)
        #               right = 3
        #       while3: mid = (3 + 3) // 2 = 3
        #               left = 4
        #               right = 3
        return left


if __name__ == "__main__":
    tests = [
        ([1,3,5,6], 5, 2),
        ([1,3,5,6], 4, 2),
        ([1,3,5,6], 2, 1),
        ([1,3,5,6], 9, 4),
    ]

    func = Solution()

    for nums, target, answer in tests:
        print(f"result: {func.searchInsert(nums, target)}, answer: {answer}")

