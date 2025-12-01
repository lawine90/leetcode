from typing import List
from itertools import combinations


"""
n명의 직원 중 자신이 설정한 출근 시간 +10분 이내에 도착하여 상품을 받는 직원의 수
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/388351
"""
from typing import List


# 개선점:
#   time_diff의 내부 구조가 불필요하게 복잡함. 단순화 필요
def time_diff(target, source):
    target_hour = int(target / 100)
    source_hour = int(source / 100)

    target_minute = target - (target_hour * 100)
    source_minute = source - (source_hour * 100)

    diff_minute = (60 * (target_hour - source_hour)) + (target_minute - source_minute)

    #return diff_minute, diff_minute <= 10
    return diff_minute <= 10


def solution(schedules, timelogs, startday):
    check = [[] for _ in range(len(schedules))]

    for t in range(len(timelogs[0])):
        if (t + startday) % 7 in [0, 6]:
            continue

        for e in range(len(schedules)):
            check[e].append(time_diff(timelogs[e][t], schedules[e]))

    return sum(all(e) for e in check)


if __name__ == "__main__":
    tests = [
        ([700, 800, 1100], [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]], 5, 3),
        ([730, 855, 700, 720], [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]], 1, 2),
    ]

    for schedules, timelogs, startday, answer in tests:
        print(f"result: {solution(schedules, timelogs, startday)}, answer: {answer}")

