from typing import List

"""
string의 가장 마지막 단어의 길이
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(' ')[-1])


if __name__ == "__main__":
    tests = [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6)
    ]

    func = Solution()

    for s, answer in tests:
        print(f"result: {func.lengthOfLastWord(s)}, answer: {answer}")

