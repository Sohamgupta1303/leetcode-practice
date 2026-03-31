class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 1) {
            return 0;
        }
        int max = 0;
        int left = 0;
        int right = 1;
        while (right < prices.size()) {
            while (prices[right] <= prices[left] && right < prices.size()) {
                left = right;
                right ++;
            }
            if (right < prices.size()) {
                max = std::max(max, prices[right] - prices[left]);
                right++;
            }
            
        }

        return max;
    }
};
