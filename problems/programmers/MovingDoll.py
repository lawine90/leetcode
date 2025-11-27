from typing import List
from itertools import combinations


"""
사라지는 인형의 갯수를 구하는 함수
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/64061
"""
from typing import List
import numpy as np


def solution(board: List[List[int]], moves: List[int]) -> int:
    board_mat = np.matrix(board)

    box = []
    removed = 0

    for j in moves:
        j_idx = j - 1

        if all(board_mat[:,j_idx] == 0):
            continue
            #print("all zero")

        i_idx = min(i for i, e in enumerate(board_mat[:,j_idx]) if e != 0)

        if len(box) != 0 and box[-1] == board_mat[i_idx,j_idx]:
            removed += 2
            box.pop()
        else:
            box.append(board_mat[i_idx,j_idx])

        board_mat[i_idx,j_idx] = 0

    return removed


if __name__ == "__main__":
    tests = [
        ([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4], 4),
    ]

    for b, m, answer in tests:
        print(f"result: {solution(b, m)}, answer: {answer}")

