class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        right = 0
        maxFreq = 0
        result = 0

        while right < len(s):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1
            maxFreq = max(count[s[right]], maxFreq)

            if (right - left + 1 - maxFreq) <= k:
                result = max(result, right - left + 1)
                right += 1
            else:
                count[s[left]] -= 1
                left += 1
                right += 1
        
        return result
            