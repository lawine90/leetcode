"""
입력된 string을 integer로 변환하는 함수를 만들자
white space는 제거.
문자열이 읽히면 그 자리에서 종료, 숫자가 읽힌 지점까지만 인트로 변환
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        s_ = s.strip()
        holder = []

        for i, c in enumerate(s_):
            if c.isdigit() or (c == '-' and i == 0) or (c == '+' and i == 0):
                holder.append(c)
            elif not c.isdigit() and i == 0:
                holder.append('0')
                break
            else:
                break

        try:
            result = int(''.join(holder))
        except:
            return 0

        if -2**31 >= result:
            return -2**31
        elif result >= 2**31 - 1:
            return 2**31 - 1
        else:
            return result


if __name__ == "__main__":
    tests = [
        ("42", 42),
        (" -42", -42),
        ("1337c0d3", 1337),
        ("words and 987", 0)
    ]

    func = Solution()

    for s, answer in tests:
        print(f"result: {func.myAtoi(s)}, answer: {answer}")

