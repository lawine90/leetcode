"""
길이 w의 창고에 n개의 상자를 쌓고 num번째 box를 꺼낼 때 총 꺼내야 하는 박스의 갯수는?
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/389478
"""
from typing import List
import numpy as np


def solution(n, w, num):
    packages = list(range(1, n+1))
    store = []

    for idx, i in enumerate(range(0, len(packages), w)):
        sub_list = packages[i:i + w]

        if len(sub_list) < w:
            sub_list.extend([0] * (w - len(sub_list)))

        if idx % 2 != 0:
            sub_list = list(reversed(sub_list))

        store.append(sub_list)

    store_mat = np.matrix(store)
    i_idx, j_idx = np.where(store_mat == num)

    return int(np.sum(store_mat[:,j_idx[0]] > num) + 1)


if __name__ == "__main__":
    tests = [
        (22, 6, 8, 3),
        (13, 3, 6, 4),
    ]

    for n, w, num, answer in tests:
        print(f"result: {solution(n, w, num)}, answer: {answer}")

