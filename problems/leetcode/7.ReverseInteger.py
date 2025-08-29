"""
입력된 integer를 역순의 integer로 생성하기
단, 역순의 integer의 값이 32비트를 넘을 경우는 0을 리턴
"""
class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            rev = int(str(x)[::-1])
        else:
            rev = int('-'+str(abs(x))[::-1])

        if not (-2**31 <= rev <= 2**31 - 1):
            return 0
        else:
            return rev


if __name__ == "__main__":
    tests = [
        (123, 321),
        (-123, -321),
        (120, 21),
    ]

    func = Solution()

    for s, answer in tests:
        print(f"result: {func.reverse(s)}, answer: {answer}")

