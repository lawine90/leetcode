from typing import List

"""
# https://leetcode.com/problems/plus-one/description/
주어진 digits를 +1을 더하여 리턴
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plused = int(''.join(map(str, digits))) + 1
        return list(map(int, str(plused)))


if __name__ == "__main__":
    tests = [
        ([4,3,2,1], [4,3,2,2]),
        ([9], [1,0]),
    ]

    func = Solution()

    for digits, answer in tests:
        print(f"result: {func.plusOne(digits)}, answer: {answer}")

