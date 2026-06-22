class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyIn = prices[0]
        profit = 0

        for price in prices:
            buyIn = min(buyIn, price)
            profit = max(profit, price - buyIn)

        return profit

