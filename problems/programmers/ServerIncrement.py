from typing import List
from itertools import combinations


"""
링크 참조
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/389479
"""
from typing import List


# 개선점:
#   dict 구조는 hash 연산 비용이 들고 문자열 포맷팅도 들어가서 비효율적. list를 쓰는게 더 효율적임
#   if m > player: 분기는 필요가 없음.
def solution(players, m, k):
    tables = {f"{i}~{i+1}": {
        "player": p,
        "server": 0,
        "increment": 0
    } for i, p in enumerate(players)}

    for i, player in enumerate(players):
        if m > player:
            server = 0
            increment = 0
        elif m <= player:
            total_server = int(player / m)
            current_server = tables[f"{i}~{i+1}"]["server"]

            if total_server > current_server:
                increment = total_server - current_server
            else:
                increment = 0

            for j in range(i, k + i):
                if j <= 23 and increment != 0:
                    #print(f"{j}~{j+1}: {tables[f'{j}~{j+1}']['server']}")
                    tables[f"{j}~{j+1}"]["server"] = tables[f"{j}~{j+1}"]["server"] + increment

        tables[f"{i}~{i+1}"]["increment"] = increment

    return sum(d["increment"] for d in tables.values())


if __name__ == "__main__":
    tests = [
        ([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5, 7),
        ([0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0], 5, 1, 11),
        ([0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 1, 1, 12),
    ]

    for players, m, k, answer in tests:
        print(f"result: {solution(players, m, k)}, answer: {answer}")

