class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (len (prices) == 1):
            return 0

        profit = 0
        i = 0
        while (i < len(prices)):
            j = i + 1
            while (j < len(prices) and prices[j] > prices[i]):
                profit = max (profit, prices[j] - prices[i])
                j += 1
            i = j

        return profit

