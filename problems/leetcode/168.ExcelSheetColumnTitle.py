from typing import List

"""
# https://leetcode.com/problems/excel-sheet-column-title/description/
컬럼의 넘버가 주어졌을 때 엑셀의 알파벳 컬럼명을 리턴 
"""
from string import ascii_uppercase


class Solution:
    def __init__(self):
        self.maps = {i+1: u for i, u in enumerate(ascii_uppercase)}

    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber <= 26:
            return self.maps[columnNumber]

        col = ''
        initNumbs = columnNumber

        while True:
            dv, lst = divmod(initNumbs, 26)

            # 나머지가 발생하지 않을 경우 'Z'를 컬럼에 넣고 몫에서 1을 차감
            if lst == 0:
                dv -= 1
                lst = 26

            col = self.maps[lst] + col

            if dv > 26:
                initNumbs = dv
            else:
                col = self.maps[dv] + col
                break

        return col


if __name__ == "__main__":
    tests = [
        (28, "AB"),
        (701, "ZY"),
    ]

    func = Solution()

    for columnNumber, answer in tests:
        print(f"result: {func.convertToTitle(columnNumber)}, answer: {answer}")

