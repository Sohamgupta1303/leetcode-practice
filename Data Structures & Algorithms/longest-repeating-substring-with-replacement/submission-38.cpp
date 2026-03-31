class Solution {
public:
    int characterReplacement(string s, int k) {
      vector<int> char_map(26, 0);
      int left = 0;
      int right = 0;
      int max_result = 0;

      while (right < s.size()) {
        char character = s[right];
        char_map[character - 'A']++;
        int max_freq = 0;
        for (int freq : char_map) {
            max_freq = std::max(max_freq, freq);
        }
        if (right + 1 - left - max_freq <= k) {
            right++;
            max_result = max(right - left, max_result);
        } else {
            char_map[s[left] - 'A']--;
            left++;
            right++;
        }
      }

      return max_result;
    }
};
