from typing import List
from itertools import combinations


"""
번역하기 복잡... 원문을 그대로 옮김
You are given N counters, initially set to 0, and you have two possible operations on them:
    increase(X) − counter X is increased by 1,
    max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:
    if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
    if A[K] = N + 1 then operation K is max counter. 
"""
def solution(N, A):
    # 아래 코드는 max(cnt)에서 cnt 전체를 훑기 때문에 시간 초과의 위험이 있음
    # # initialize counter
    # cnt = [0] * N
    #
    # for i in range(len(A)):
    #     if A[i] <= N:
    #         cnt[A[i]-1] += 1
    #     else:
    #         cnt = [max(cnt)] * N
    #
    # return cnt

    base_value = 0
    cnt = [base_value] * N
    max_value = 0

    for e in A:
        if e <= N:
            cnt[e - 1] += 1
            base_value += 1

            if cnt[e - 1] >= max_value:
                max_value = cnt[e - 1]
        else:
            cnt = [max_value] * N

    return cnt


if __name__ == "__main__":
    tests = [
        ([3, 4, 4, 6, 1, 4, 4], 5, [3, 2, 2, 4, 2]),
    ]

    for A, N, answer in tests:
        print(f"result: {solution(N, A)}, answer: {answer}")

