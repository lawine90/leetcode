from typing import List

"""
입력된 list of int로 bar chart를 그린다고 가졍했을 때, 가장 넓이가 넓은 값을 구하라
여기서 포인트는 메모리 효율화임. 아래 주석처리된 부분도 동작은 잘 되나 list를 두개나 별도로 저장해서 써서 메모리가 오버됨
이를 while 문으로 두 개의 포인터가 left, right에서 조금씩 움직이며 최대값을 찾아나가는게 핵심 
"""
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         current_area = 0

#         if len(height) >= 15:
#             import numpy as np
#             height_idx = [
#                 (i, h)
#                 for i, h in enumerate(height)
#                 if h >= np.mean(height)
#             ]
#         else:
#             height_idx = list(enumerate(height))
#
#         for i, y1 in height_idx:
#             left_height = height_idx[i+1:]
#             for j, y2 in left_height:
#                 current_area = max(current_area, min(y1, y2) * (j - i))
#
#         return current_area

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        current_area = 0

        while left < right:
            current_area = max(current_area, (right - left) * min(height[right], height[left]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return current_area


if __name__ == "__main__":
    tests = [
        ([1,8,6,2,5,4,8,3,7], 49),
        ([1,1], 1),
    ]

    func = Solution()

    for s, answer in tests:
        print(f"result: {func.maxArea(s)}, answer: {answer}")

