from typing import List
from itertools import combinations


"""
사람의 수 n과 단어의 list words가 주어졌을 때 탈락자의 번호와 탈락이 발생한 라운드를 return하는 함수
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12981
"""
from typing import List


def solution(n: int, words: List[str]) -> List[int]:
    # 개선점: list 말고 set을 쓰면 자료구조상 검색 속도가 더 빠름
    #talked = []
    talked = set()

    for i, w in enumerate(words):
        if i == 0:
            #talked.append(w)
            talked.add(w)
            continue

        if w not in talked and w[0] == words[i-1][-1]:
            #talked.append(w)
            talked.add(w)
        elif w in talked or w[0] != words[i-1][-1]:
            rnd = (i // n) + 1      # 라운드
            person_i = (i % n) + 1  # 사람
            return [person_i, rnd]

    # 틀린 사람이 없으면 [0,0]
    return [0, 0]


if __name__ == "__main__":
    tests = [
        (3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"], [3,3]),
        (5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"], [0,0]),
        (2, ["hello", "one", "even", "never", "now", "world", "draw"], [1,3])
    ]

    for n, words, answer in tests:
        print(f"result: {solution(n, words)}, answer: {answer}")

