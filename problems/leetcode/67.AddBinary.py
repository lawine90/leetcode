from typing import List

"""
# https://leetcode.com/problems/add-binary/
주어진 두 binary 값을 합하여 binary로 리턴
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    tests = [
        ('11', '1', '100'),
        ('1010', '1011', '10101'),
    ]

    func = Solution()

    for a, b, answer in tests:
        print(f"result: {func.addBinary(a, b)}, answer: {answer}")

