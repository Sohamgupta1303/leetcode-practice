class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) is 1:
            return 0;

        left = 0;
        right = left + 1;
        maxProfit = 0;

        while (right < len(prices)):
            if (prices[right] - prices[left] < 0):
                left = right;
                right += 1;
            else:
                if (prices[right] - prices[left] > maxProfit):
                    maxProfit = prices[right] - prices[left];
                right += 1;

        return maxProfit

        