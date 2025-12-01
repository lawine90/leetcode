from typing import List
from itertools import combinations


"""
링크 참조
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/389480
"""
from typing import List


def solution(info: List[List[int]], n: int, m: int) -> int:
    # 초기 상태: B 흔적 0일 때, A 흔적 0
    # states = { B의_누적_흔적 : A의_최소_흔적 }
    states = {0: 0}

    # 모든 물건을 하나씩 순회
    for trace_a, trace_b in info:
        next_states = {}

        # 현재 가능한 모든 상태(case)를 꺼내서 확인
        for current_b, current_a in states.items():
            # {0: 1, 2: 0}

            # Case 1: 이번 물건을 A가 훔치는 경우
            new_a = current_a + trace_a
            new_b = current_b  # B는 그대로

            # 1 + 2 -> 0 + 2
            # 0     -> 2

            # A가 제한(n)을 넘지 않을 때만 유효
            if new_a < n:
                # 같은 B 흔적일 때 A 흔적이 더 작다면 갱신 (또는 처음 등록)
                if new_b not in next_states or new_a < next_states[new_b]:
                    next_states[new_b] = new_a
                    # {0: 3} -> {0: 3, 3: 1, 2: 2}

            # Case 2: 이번 물건을 B가 훔치는 경우
            new_a = current_a  # A는 그대로
            new_b = current_b + trace_b

            # 1      -> 0
            # 0 + 3  -> 2 + 3

            # B가 제한(m)을 넘지 않을 때만 유효
            if new_b < m:
                # 같은 B 흔적일 때 A 흔적이 더 작다면 갱신
                if new_b not in next_states or new_a < next_states[new_b]:
                    next_states[new_b] = new_a
                    # {0: 3, 3: 1}

        # 다음 물건으로 넘어가기 위해 상태 업데이트
        states = next_states
        #print(states.items())

    # 모든 물건을 다 털었는데 가능한 상태가 하나도 없다면 -1
    if not states:
        return -1

    # 남은 상태들 중 A의 흔적(Value)의 최솟값 반환
    return min(states.values())


if __name__ == "__main__":
    tests = [
        ([[1, 2], [2, 3], [2, 1]], 4, 4, 2),
        ([[1, 2], [2, 3], [2, 1]], 1, 7, 0),
        ([[3, 3], [3, 3]], 7, 1, 6),
        ([[3, 3], [3, 3]], 6, 1, -1),
    ]

    for info, n, m, answer in tests:
        print(f"result: {solution(info, n, m)}, answer: {answer}")

