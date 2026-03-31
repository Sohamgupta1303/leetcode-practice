class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = left + 1;
        int max = 0;

        while (right < prices.length) {
            if (prices[right] > prices[left]) {
                max = Math.max(prices[right] - prices[left], max);
            } else {
                left = right;
            }
            right++;
        }

        return max;
    }
}
