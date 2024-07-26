class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_start = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if min_start > prices[i]:
                min_start = prices[i]
            if max_profit < prices[i] - min_start:
                max_profit = prices[i] - min_start
        print(min_start, max_profit)
        return max_profit