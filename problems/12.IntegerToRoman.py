from typing import List

"""
입력된 숫자를 roman 숫자로 변환하는 함수.
주의점은 값이 4 또는 9일 경우 특수한 처리가 필요하다는 것.
어떤 특수처리를 해야하는지는 문제 참조:  https://leetcode.com/problems/integer-to-roman/
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = {
            1000: "M",
            500: "D",
            100: "C",
            50: "L",
            10: "X",
            5: "V",
            1: "I"
        }

        holder = []

        for i, k in enumerate(roman_map.keys()):
            # 숫자의 맨 첫 글자가 4인 경우
            # 단, k가 500, 50, 5인 경우 처리하면 꼬이게 되니까 divmod(num, k)[0] 이 0이 아닐 때 처리하도록 조건문 추가
            # e.g. 40의 경우, k값이 50일때는 처리되지 않고 넘어감
            #   k값이 10일때 몫이 0이 아니므로 조건문 안으로 들어가서 실행하게 됨
            #   k값이 10일때 그 이전의 k값을 찾음 (tmp_k = 50)
            #   이를 바탕으로 roman_map[k] + roman_map[tmp_k]로 40 -> XL로 변환
            #   변환한 후 num 값에서 40 (4 * k)를 빼줘서 num을 업데이트
            if str(num)[0] == '4' and divmod(num, k)[0] != 0:
                tmp_k = list(roman_map.keys())[i-1]
                # print(f"tmp_k in 4: {tmp_k}")

                holder.append(roman_map[k] + roman_map[tmp_k])
                num = num - (4*k)
            # 숫자의 맨 첫 글자가 9인 경우
            # 단, k가 500, 50, 5인 경우 처리해야되므로 divmod(num, k)[0] != 0 조건문 추가
            # e.g. 9의 경우, k값이 5일때는 몫이 1이므로 !=0 조건을 만족해서 조건문 안으로 들어감
            #   k값이 5일때 목이 0이 아니므로 조건문 안으로 들어가서 실행하게 됨
            #   k = 5 앞 뒤의 key값 (tmp_k1, tmp_k2)를 찾음
            #   이를 바탕으로 roman_map[tmp_k2] + roman_map[tmp_k1] 로 9 -> IX 변환
            #   변환 후 num에서 9를 빼줘어 num 값을 업데이트
            elif str(num)[0] == '9' and divmod(num, k)[0] != 0:
                tmp_k1 = list(roman_map.keys())[i-1]
                tmp_k2 = list(roman_map.keys())[i+1]
                # print(f"k in 9: {k}")
                # print(f"tmp_k in 9: {tmp_k1}, {tmp_k2}")

                holder.append(roman_map[tmp_k2] + roman_map[tmp_k1])
                num = num - (9*tmp_k2)
            else:
                tmp_val, num = divmod(num, k)
                holder.append(roman_map[k] * tmp_val)

        return ''.join(holder)


if __name__ == "__main__":
    tests = [
        (3749, 'MMMDCCXLIX'),
        (58, 'LVIII'),
        (1994, 'MCMXCIV'),
    ]

    func = Solution()

    for s, answer in tests:
        print(f"result: {func.intToRoman(s)}, answer: {answer}")

