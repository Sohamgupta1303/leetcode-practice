class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int max = 0;
        unordered_set<int> numbers;

        for (int num : nums) {
            numbers.insert(num);
        }
        for (int num : nums) {
            if (!numbers.count(num + 1)) {
                int count = 0;
                int traverse = num;
                while (numbers.count(traverse)) {
                    count++;
                    traverse--;
                }
                max = std::max(max, count);
            } 
        }
        return max;
    }
};
