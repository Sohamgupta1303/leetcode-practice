class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> ret = vector<int>(temperatures.size());
        for (int i = 0; i < temperatures.size(); i++) {
            for (int j = i + 1 ; j < temperatures.size(); j++) {
                if (temperatures[j] > temperatures[i]) {
                    ret[i] = j - i;
                    break;
                }
            }
        }
        return ret;
    }
};
