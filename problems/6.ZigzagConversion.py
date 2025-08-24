"""
입력된 문자열을 지그재그로 나열하기...
설명하기 복잡하니 릿코드의 문제 설명 참조..
https://leetcode.com/problems/zigzag-conversion/description/
"""
import numpy as np


class Solution:
    """
    여기서 주목했던 점: 조금 로직이 복잡하더라도 설명 가능하게 구현을 해보자..
    """
    def convert(self, s: str, numRows: int) -> str:
        # 문자열이 너무 짧거나 numRows가 1인 경우는 입력된 문자열을 그대로 반환하면 된다.
        if len(s) == 1 or numRows == 1 or numRows >= len(s):
            return s

        # numRows가 2밖에 안될 경우 간단한 로직이므로 2인 경우는 따로 처리한다
        if numRows == 2:
            ss = s
            string_holders = []

            while True:
                if len(list(ss[:2])) == 2:
                    # 자른 문자열의 길이가 2인 경우 그대로 홀더에 어펜드
                    string_holders.append(list(ss[:2]))
                else:
                    # 자른 문자열이 1인 경우는 빈 값을 하나 더 추가해준 뒤에 어펜드
                    string_holders.append(list(ss[:2]) + [''])
                ss = ss[2:]
                if ss == '':
                    break

            # list of list를 전치한 다음 join
            return ''.join([''.join(a) for a in np.transpose(string_holders)])

        # numRows가 3 이상인 경우, 중간중간 지그재그패턴이 있으므로 몇번이나 반복해줘야 하는지 계산
        repeat_times, leaved = divmod(len(s), numRows)
        num_holders = []

        for i in range(max(repeat_times-1, 5)):
            num_holders.append(numRows)
            for j in range(numRows-2):
                num_holders.append(1)

        num_holders.append(leaved)

        # 지그재그패턴이 발생하는 경우 문자열을 어디에 넣어줄지 미리 인덱스를 계산
        leave_idxs = [d if d == 0 else d + 1 for d, e in enumerate(num_holders[:numRows-1])] * (len(num_holders))
        string_holders = []
        ss = s

        for i, idx in enumerate(num_holders):
            # 문자열을 그대로 넣어도 되는 경우
            if idx == numRows:
                dlatl = list(ss[:numRows])
                if len(dlatl) == numRows:
                    string_holders.append(dlatl)
                else:
                    dlatl2 = dlatl + [''] * (numRows - len(dlatl))
                    string_holders.append(dlatl2)
                ss = ss[numRows:]
                if ss == '': break
            # 지그재그 패턴이 발생하는 경우
            elif idx != numRows and idx == 1:
                # 빈 값으로 리스트 생성
                tmp = [''] * numRows

                # 특정 위치에 캐릭터 추가
                tmp[-leave_idxs[i]] = ss[0]

                # 홀더에 어펜드
                string_holders.append(tmp)
                ss = ss[1:]
                if ss == '': break
            elif idx != numRows and idx != 1:
                skajwl = list(ss[:idx])
                string_holders.append(skajwl + [''] * (numRows - len(skajwl)))
                ss = ''

        print(np.transpose(string_holders))
        return ''.join([''.join(a) for a in np.transpose(string_holders)])


if __name__ == "__main__":
    tests = [
        ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'),
        ('PAYPALISHIRING', 4, 'PINALSIGYAHRPI'),
    ]

    func = Solution()

    for s, numRow, answer in tests:
        print(f"result: {func.convert(s, numRow)}, answer: {answer}")

