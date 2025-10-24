from typing import List

"""
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
주어진 패턴이 가장 빠르게 등장하는 인덱스 찾기
e.g. haystack = "sadbutsad", needle = "sad"
    output: 0
"""


# 가장 쉬운 방법: python 내장 함수인 .find를 사용한다.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


# 생각을 좀 해볼 방법: 주어진 문자열을 돌면서 찾는다
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            # print(f"{i}, {haystack[i:i+len(needle)]}")
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


if __name__ == "__main__":
    tests = [
        (1, ["()"]),
        (3, ["((()))","(()())","(())()","()(())","()()()"]),
    ]

    func = Solution()

    for s, answer in tests:
        print(f"result: {func.generateParenthesis(s)}, answer: {answer}")

