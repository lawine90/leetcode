from typing import List

"""
리스트에 들어있는 여러 문자열의 가장 긴 공통의 prefix를 찾는 문제
아래 주석처리된 코드도 동작하긴 하지만 time exceed 에러가 발생함
대신 3개의 포인터를 사용해서 패턴을 찾는 방식으로 변경
"""
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         from itertools import combinations

#         nums.sort()

#         result = [tuple(sorted(t)) for t in combinations(nums, 3) if sum(t) == 0]
#         return list(set(result))

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         results = []
#         left = 0
#         right = len(nums) - 1
#
#         nums.sort()
#
#         while right > left:
#             left_val = nums[left]
#             right_val = nums[right]
#
#             if (left_val + right_val) * (-1) in nums[left+1:right] and \
#                     tuple(sorted((nums[left], nums[right], -(left_val + right_val)))) not in results:
#                 print(f"left: {left_val}, right: {right_val}")
#                 results.append(tuple(sorted((nums[left], nums[right], -(left_val + right_val)))))
#
#             if left_val + right_val >= 0:
#                 right -= 1
#             else:
#                 left += 1
#
#         return results

class Solution:
    def threeSum(self, nums):
        nums.sort()
        T = []

        # 포인터가 3개이니 len(nums - 2)까지만 루프를 진행
        for i in range(len(nums)-2):
            if 0 < i and nums[i] == nums[i-1]:
                continue

            # i는 가장 left에 있는 pointer
            # l은 i+1 pointer, r은 가장 right에 있는 pointer
            # e.g. [-4, -3, -1, 0, 1, 2, 4, 7]
            # i: 0   i   l                  r
            # i: 1       i   l           r
            l, r = i+1, len(nums)-1

            while l < r:
                if nums[i]+nums[l]+nums[r] > 0:
                    r -= 1
                elif nums[i]+nums[l]+nums[r] < 0:
                    l += 1
                else:
                    T.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return T


if __name__ == "__main__":
    tests = [
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        ([0,1,1], []),
        ([0,0,0], [0,0,0]),
    ]

    func = Solution()

    for s, answer in tests:
        print(f"result: {func.threeSum(s)}, answer: {answer}")

