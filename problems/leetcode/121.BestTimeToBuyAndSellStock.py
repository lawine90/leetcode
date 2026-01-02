from typing import List

"""
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
주식 가격 list가 주어졌을 때, 가장 최대 이익이 되는 구매/판매를 return 
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sorted_prices = sorted(prices, reverse=True)

        # # edge case
        # if sorted_prices == prices:
        #     return 0

        # buy_day = 0
        # sell_day = buy_day + 1
        # result = 0

        # while True:
        #     profit = prices[sell_day] - prices[buy_day]
        #     #print(f"profit: {profit}, sell: {prices[sell_day]} buy: {prices[buy_day]}")

        #     if profit > result:
        #         result = profit

        #     if sell_day != len(prices)-1:
        #         sell_day += 1
        #     elif sell_day == len(prices)-1 and buy_day != len(prices)-2:
        #         buy_day += 1
        #         sell_day = buy_day + 1
        #     elif (sell_day == len(prices)-1) and (buy_day == len(prices)-2):
        #         break

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit


if __name__ == "__main__":
    tests = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
    ]

    func = Solution()

    for prices, answer in tests:
        print(f"result: {func.maxProfit(prices)}, answer: {answer}")

