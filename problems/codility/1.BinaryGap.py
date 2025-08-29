from typing import List
from itertools import combinations


"""
입력된 integer를 binary로 바꾼 뒤 두 개의 1 사이에 0이 몇개 있는지 카운트하고 가장 큰 gap을 찾아라
"""
def solution(N):
    # convert int to binary
    bin_n = format(N, "b")
    #print(f"binary n: {bin_n}")

    # check longest gap
    gap = 0
    zeros = 0
    state = 0

    for c in bin_n:
        if c == '1' and state == 0:
            state = 1
        elif c == '1' and state != 0:
            #print(f"current gap: {gap}, new gap: {zeros}")
            gap = max(gap, zeros)
            zeros = 0
        elif c == '0' and state == 0:
            next
        elif c == '0' and state != 0:
            zeros += 1

    return gap


if __name__ == "__main__":
    tests = [
        (1041, 5),
        (647, 4),
    ]

    for nums, answer in tests:
        print(f"result: {solution(nums)}, answer: {answer}")

