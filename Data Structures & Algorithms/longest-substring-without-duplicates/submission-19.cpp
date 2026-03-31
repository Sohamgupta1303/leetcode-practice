class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> letters;
        int max = 0;
        int left = 0;
        int right = 0;

        while (right < s.length()) {
            if (!letters.count(s[right])) {
                letters.insert(s[right]);
                right++;
                max = std::max(max, right - left);
            } else {
                max = std::max(max, right - left);
                while (s[left] != s[right]) {
                    letters.erase(s[left]);
                    left++;
                }
                left++;
                right++;
            }
            
        }

        return max;
        /*
        au
        */
    }
};
