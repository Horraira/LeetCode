from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = prices[0], 0
        for price in prices:
            if price < buy:
                buy = price
            elif price - buy > profit:
                profit = price - buy

        return profit

solution = Solution()
prices = [2,4,1]
print(solution.maxProfit(prices))