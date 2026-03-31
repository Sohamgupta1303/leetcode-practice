class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> number_and_freq;
        vector<vector<int>> bucket(nums.size(), vector<int>(0));
        for (int num : nums) {
            number_and_freq[num] ++;
        }
        for (const auto& pair : number_and_freq) {
            int freq = pair.second;
            int number = pair.first;
            bucket[freq - 1].push_back(number);
        }
        int k_traversal = 0;
        vector<int> result(k);
        for (int i = bucket.size() - 1; i > -1; i--) {
            if (bucket[i].size() != 0) {
                nums = bucket[i]; // nums is a vector of numbers with frequency i
                for (int num : nums) {
                    result[k_traversal] = num;
                    k_traversal ++ ;
                }
                if (k_traversal == k) {
                    return result;
                }
            }
        }

        return result;
    }
};
