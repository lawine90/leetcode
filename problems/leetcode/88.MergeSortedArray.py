from typing import List

"""
# https://leetcode.com/problems/merge-sorted-array/
in-place로 nums2의 element를 nums1에 오름차순으로 넣기.
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """

        def binSearch(nums, target):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1

            return left

        for _ in range(n):
            nums1.pop(-1)

        for n2 in nums2:
            if n2 in nums1:
                nums1.insert(nums1.index(n2) + 1, n2)
            else:
                insert_idx = binSearch(nums1, n2)
                print(insert_idx, n2)
                nums1.insert(insert_idx, n2)
                print(nums1)

        return nums1


if __name__ == "__main__":
    tests = [
        ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
        ([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3, [-1,0,0,1,2,2,3,3,3]),
    ]

    func = Solution()

    for nums1, m, nums2, n, answer in tests:
        print(f"result: {func.merge(nums1, m, nums2, n)}, answer: {answer}")

