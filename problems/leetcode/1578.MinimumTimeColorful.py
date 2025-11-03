from typing import List

"""
# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description
연속해서 중복된 색상이 나오지 않도록 문자열을 제거하고 해당 문자열을 제거하는 최소 시간을 계산하기
e.g. colors = "abaac", neededTime = [1,2,3,4,5]
    output: 3
"""


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        colors_list = list(colors)
        n = len(colors_list)
        durations = 0

        i, j = 0, 1

        # 리스트 끝까지 돌면서 중복된 문자열이 발견될 경우 삭제한다
        while j + 1 <= n:
            if colors_list[i] != colors_list[j]:
                i += 1
                j += 1
            else:
                if neededTime[i] > neededTime[j]:
                    durations += neededTime[j]

                    del colors_list[j]
                    del neededTime[j]
                    n = len(colors_list)
                else:
                    durations += neededTime[i]

                    del colors_list[i]
                    del neededTime[i]
                    n = len(colors_list)

        return durations


if __name__ == "__main__":
    tests = [
        ("abaac", [1,2,3,4,5], 3),
        ("aabaa", [1,2,3,4,1], 2),
    ]

    func = Solution()

    for s, t, answer in tests:
        print(f"result: {func.minCost(s, t)}, answer: {answer}")

