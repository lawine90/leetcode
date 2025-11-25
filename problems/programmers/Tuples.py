from typing import List
from itertools import combinations


"""
문자열로 표현된 주어진 집합 s에서 tuple을 생성하기
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/64065
    주의?점: 집합 s의 순서는 뒤죽박죽이지만 tuple은 순서가 있으므로 [1,2,3] != [3,1,2] 이다
"""
from typing import List


def solution(s: str) -> List[int]:
    result = []

    for e in sorted(s.strip('{}').split('},{'), key=lambda x: len(x)):
        vals = e.split(',')

        for sub_e in vals:
            num = int(sub_e)

            if num not in result:
                result.append(num)

    return result


if __name__ == "__main__":
    tests = [
        ("{{2},{2,1},{2,1,3},{2,1,3,4}}", [2, 1, 3, 4]),
        ("{{1,2,3},{2,1},{1,2,4,3},{2}}", [2, 1, 3, 4]),
        ("{{20,111},{111}}", [111, 20]),
        ("{{123}}", [123]),
        ("{{4,2,3},{3},{2,3,4,1},{2,3}}", [3, 2, 4, 1]),
    ]

    for nums, answer in tests:
        print(f"result: {solution(nums)}, answer: {answer}")

