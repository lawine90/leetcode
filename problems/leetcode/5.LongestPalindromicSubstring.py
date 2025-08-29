"""
입력된 문자열 중 앞뒤로 똑같은 가장 긴 문자열 찾아내기
palindromic string이란? 정과 역이 똑같은 문자열 (회문)
    e.g. 기울기, 토마토, 스위스
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 입력된 문자열이 그대로 회문일 경우 입력 값을 리턴
        if s == s[::-1]:
            return s

        # 회문을 저장할 리스트 초기화
        len_list = []

        for i, c1 in enumerate(s):
            # 첫번째 문자를 제외한 substring 저장
            sub_s = s[i+1:]
            len_list.append(c1)

            for j, c2 in enumerate(sub_s):
                if c1+sub_s[:j+1] == (c1+sub_s[:j+1])[::-1]:
                    len_list.append(c1+sub_s[:j+1])

        return sorted(len_list, key=lambda x: len(x))[-1]


if __name__ == "__main__":
    tests = [
        ('babad', 'bab'),
        ('cbbd', 'bb'),
    ]

    func = Solution()

    for s, answer in tests:
        print(f"result: {func.longestPalindrome(s)}, answer: {answer}")

