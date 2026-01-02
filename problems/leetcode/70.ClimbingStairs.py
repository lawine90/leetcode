from typing import List

"""
# https://leetcode.com/problems/climbing-stairs/description/
계단 오르기 DP 문제
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # edge cases
        if n <= 3:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        print(dp)

        return dp[-1]


if __name__ == "__main__":
    tests = [
        (2, 2),
        (3, 3),
        (5, 8),
    ]

    func = Solution()

    for n, answer in tests:
        print(f"result: {func.climbStairs(n)}, answer: {answer}")

