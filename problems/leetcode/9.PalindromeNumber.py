
"""
left to right, right to left 모두 동일한 숫자 찾기
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        reversed_x = ''.join(list(reversed(str_x)))
        return str_x == reversed_x


if __name__ == "__main__":
    tests = [
        (121, True),
        (-121, False),
        (1331, True),
    ]

    func = Solution()

    for s, answer in tests:
        print(f"result: {func.isPalindrome(s)}, answer: {answer}")

