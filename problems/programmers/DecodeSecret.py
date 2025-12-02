from typing import List
from itertools import combinations


"""
링크 참조
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/388352
"""
from typing import List


from itertools import combinations


def intersect(l1, l2):
    return len([e for e in l1 if e in l2])


# 개선점:
#   comb2 생성 로직의 비효율성:
#   if m > player: 분기는 필요가 없음.
def solution(n, q, ans):
    max_idx = ans.index(max(ans))

    #print(list(combinations(q[max_idx], ans[max_idx])))

    # for i, comb in enumerate(q):
    #     print(list(combinations(comb, ans[i])))

    result = []

    for comb in combinations(q[max_idx], ans[max_idx]):
        #for i in range(1, n+1):
        for comb2 in combinations([e for e in range(1, n+1) if e not in comb], 5 - ans[max_idx]):
            if intersect(comb, comb2) != 0:
                continue

            candidate = sorted(comb + comb2)

            if all(intersect(candidate, l2) == a for l2, a in zip(q, ans)):
                result.append(candidate)

    #print(result)
    return len(result)


if __name__ == "__main__":
    tests = [
        (10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3], 3),
        (15, [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]], [2, 1, 3, 0, 1], 5),
    ]

    for n, q, ans, answer in tests:
        print(f"result: {solution(n, q, ans)}, answer: {answer}")

