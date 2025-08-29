"""
입력된 문자열 중 중복이 없이 가장 긴 문자열의 길이 찾아내기
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 빈 문자열이 입력된 경우 0을 리턴
        if s == '':
            return 0

        # 문자열을 임시로 담아둘 char_set과 문자열의 길이 list 초기화
        char_set = set()
        len_list = []

        for i, c1 in enumerate(s):
            # 루프 중 첫번째 문자를 set에 저장
            char_set.add(c1)

            # 루프 중 첫번째 문자를 제외한 substring 생성
            sub_s = s[i+1:]

            # 첫번째 문자의 길이를 len_list에 저장
            len_list.append(len(char_set))

            for j, c2 in enumerate(sub_s):
                # substring을 훑어가며 문자가 char_set에 없을 경우 char_set에 저장
                if sub_s[j] not in char_set:
                    char_set.add(sub_s[j])
                # substring의 문자가 char_set에 있을 경우
                #   이전까지 char_set에 저장된 문자의 길이를 저장한뒤 char_set 리셋
                #   리셋 이후엔 두번째 루프를 벗어남
                else:
                    len_list.append(len(char_set))
                    char_set = set()
                    break

        return max(len_list)


if __name__ == "__main__":
    tests = [
        ('abcabcbb', 3),
        ('bbbbb', 1),
        ('pwwkew', 3),
    ]

    func = Solution()

    for s, answer in tests:
        print(f"result: {func.lengthOfLongestSubstring(s)}, answer: {answer}")

