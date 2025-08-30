from typing import List
from itertools import combinations


"""
개구리가 현재 위치 X에서 거리 30만큼 뛰어서 목적지 Y에 도달하거나 넘을때 까지 점프한 횟수
e.g. X, Y, D = 10, 85, 30
"""
def solution(X, Y, D):
    q, r = divmod((Y - X), D)
    if r != 0:
        return q + 1
    else:
        return q


if __name__ == "__main__":
    tests = [
        (10, 85, 30, 3),
    ]

    for x, y, d, answer in tests:
        print(f"result: {solution(x, y, d)}, answer: {answer}")

