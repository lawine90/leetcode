from typing import List

"""
주어진 리스트의 int 값을 합해서 target 값과 가장 비슷한 3개의 element 합을 return하는 함수
e.g. nums = [-1, 2, 1, -4], target = 1 --> sum([-1, 2, 1]) = 2
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        # 초기값 생성: 가장 diff가 적은 sum과 target과 sum의 diff를 초기화
        closest_sum = float('inf')
        min_diff = float('inf')

        # 리스트를 돌아가면서 전체 조합을 확인
        # e.g. [-1, 2, 1, -4]
        #        i  j      k
        #        i  j  k
        #           i  j   k
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            # prev_diff = None
            # prev_sum = None

            #while j != k:
            while j < k:
                # 현재 루프에서의 합과 target과의 차이 계산
                current_sum = nums[i] + nums[j] + nums[k]
                current_diff = abs(target - current_sum)

                # if prev_diff is not None and prev_diff < current_diff:
                #     return prev_sum

                # 현재 루프에서의 diff가 더 작을 경우 min_diff와 closest_sum tnwjd
                if current_diff < min_diff:
                    min_diff = current_diff
                    closest_sum = current_sum

                # target이 더 큰 경우, current_sum의 값을 키워야 하니 j를 +1
                # target이 더 작은 경우, current_sum의 값을 줄여야 하니 k를 -1
                if current_sum < target:
                    j += 1
                else:
                    k -= 1

        return closest_sum


if __name__ == "__main__":
    tests = [
        ([-1, 2, 1, -4], 1, 2),
        ([0,0,0], 1, 0),
    ]

    func = Solution()

    for nums, target, answer in tests:
        print(f"result: {func.threeSumClosest(nums, target)}, answer: {answer}")

