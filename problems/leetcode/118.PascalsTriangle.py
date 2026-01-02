from typing import List

"""
# https://leetcode.com/problems/pascals-triangle/description/
주어진 numRows에 맞게 위의 두 값을 합하여 아래 값을 생성하는 Pascal Triangle을 list of list로 반환
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]

        init = [[1], [1,1]]

        for i in range(2, numRows):
            # left element
            temp_list = [1]

            # middle element
            for j in range(len(init[i-1])-1):
                temp_list.append(init[i-1][j] + init[i-1][j+1])

            # right element
            temp_list.append(1)

            # append to list
            init.append(temp_list)

        return init


if __name__ == "__main__":
    tests = [
        (5, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),
        (1, [[1]]),
    ]

    func = Solution()

    for numRows, answer in tests:
        print(f"result: {func.generate(numRows)}, answer: {answer}")

