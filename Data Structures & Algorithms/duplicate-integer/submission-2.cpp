class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> vals;
        for (int i : nums) {
            if (vals.count(i)) {
                return true;
            }
            vals.insert(i);
        }
        return false;
    }
};