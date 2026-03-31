class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix(nums.size(), 0);
        vector<int> postfix(nums.size(), 0);

        for (int i = 0; i < nums.size(); i++) {
            int length = nums.size();
            if (i == 0) {
                prefix[0] = nums[0];
                postfix[length - 1] = nums[length - 1];
            }
            else {
                prefix[i] = nums[i] * prefix[i - 1];
                postfix[length - 1 - i] = nums[length - 1 - i] * postfix[length - i];
            }
        }

        vector<int> result(nums.size(), 0);
        for (int i = 1; i < nums.size() - 1; i++) {
            result[i] = prefix[i - 1] * postfix[i + 1];
        }
        result[0] = postfix[1];
        result[nums.size() - 1] = prefix[nums.size() - 2];

        return result;
    }
};
