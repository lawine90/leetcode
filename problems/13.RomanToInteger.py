from typing import List

"""
입력된 숫자를 roman 숫자로 변환하는 함수.
주의점은 값이 4 또는 9일 경우 특수한 처리가 필요하다는 것.
어떤 특수처리를 해야하는지는 문제 참조:  https://leetcode.com/problems/integer-to-roman/
"""


class Solution:
    def __init__(self):
        # self.roman_map = {
        #     1000: "M",
        #     500: "D",
        #     100: "C",
        #     50: "L",
        #     10: "X",
        #     5: "V",
        #     1: "I"
        # }
        # self.roman_rev_map = {value: key for key, value in roman_map.items()}

        self.roman_rev_map = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        self.specials = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

    def romanToInt(self, s: str) -> str:
        val = 0
        s_ = s

        for key in self.specials.keys():
            if key in s_:
                val += self.specials[key]
                s_ = s_.replace(key, '')

        for c in s_:
            val += self.roman_rev_map[c]

        return val


if __name__ == "__main__":
    tests = [
        ('MMMDCCXLIX', 3749),
        ('LVIII', 58),
        ('MCMXCIV', 1994),
    ]

    func = Solution()

    for s, answer in tests:
        print(f"result: {func.romanToInt(s)}, answer: {answer}")

