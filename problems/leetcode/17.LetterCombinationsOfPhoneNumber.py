from typing import List
from itertools import product

"""
주어진 digits에 따라 영문 핸드폰 키패드에서 가능한한 모든 조합을 리턴
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
e.g. digits = '23' -> ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""


class Solution:
    def __init__(self):
        self.phone_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        alphabets = [list(self.phone_map[d]) for d in digits]
        return [''.join(c) for c in product(*alphabets)]


if __name__ == "__main__":
    tests = [
        ('23'),
        ('24'),
        ('98'),
    ]

    func = Solution()

    for nums in tests:
        print(f"result: {func.letterCombinations(nums)}")

