from typing import List

"""
주어진 숫자에 따라 짝이 맞은 괄호 조합을 모두 찾는 함수 생성하기
e.g. n = 3, result = ["((()))","(()())","(())()","()(())","()()()"]
    "(()))(" 이런 짝이 맞지 않는 조합은 안 됨.
"""


class Solution:
    @staticmethod
    def generateParenthesis(n: int) -> List[str]:
        results = []

        def backtrack(path, a, b):
            if len(path) == n * 2:
                results.append(path)
                return

            if a < n:
                backtrack(path + '(', a+1, b)
            if b < a:
                backtrack(path + ')', a, b+1)

        backtrack('(', 1, 0)
        return results


if __name__ == "__main__":
    tests = [
        (1, ["()"]),
        (3, ["((()))","(()())","(())()","()(())","()()()"]),
    ]

    func = Solution()

    for s, answer in tests:
        print(f"result: {func.generateParenthesis(s)}, answer: {answer}")

