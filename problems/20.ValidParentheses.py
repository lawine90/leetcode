from typing import List

"""
괄호가 완결성이 있는지 체크하는 문제
괄호가 열리면 무조건 닫혀야하며 짝이 맞는 괄호와 닫혀야 한다.
"""
class Solution:
    def __init__(self):
        self.holder = []
        self.opener = ['(', '[', '{']
        self.ender = [')', ']', '}']
        self.comp = [
            o+e
            for o, e in zip(self.opener, self.ender)
        ]

    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        for c in s:
            if c in self.opener:
                self.holder.append(c)
            elif c in self.ender:
                if len(self.holder) == 0:
                    return False
                elif self.holder[-1]+c in self.comp:
                    del self.holder[-1]
                else:
                    return False

        if len(self.holder) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    tests = [
        ("()", True),
        ("([])", True),
        ("([)]", False),
        ("()[]{}", True),
    ]

    func = Solution()

    for s, answer in tests:
        print(f"result: {func.isValid(s)}, answer: {answer}")

