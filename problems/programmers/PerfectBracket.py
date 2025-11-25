from typing import List
from itertools import combinations


"""
괄호로 이루어진 문자열 s가 완벽한 괄호 문자열인지 평가하는 함수 생성
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12909
"""


def solution(s: str) -> bool:
    if s[0] == ')':
        return False

    right = 1

    for char in s[1:]:
        if char == '(':
            right += 1
        elif char == ')' and right > 0:
            right -= 1
        elif char == ')' and right == 0:
            return False

    if right == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    tests = [
        ("()()", True),
        ("(())()", True),
        (")()(", False),
        ("(()(", False),
    ]

    for s, answer in tests:
        print(f"result: {solution(s)}, answer: {answer}")

