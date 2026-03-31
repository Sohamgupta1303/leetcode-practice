class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter_and_freq = {};
        left = 0;
        right = 0;
        ret = 0;

        while right < len(s):
            letter_and_freq[s[right]] = 1 + letter_and_freq.get(s[right], 0);
            if right - left + 1 - max(letter_and_freq.values())> k:
                letter_and_freq[s[left]] -= 1;
                left += 1;
            ret = max(ret, right - left + 1);
            right += 1
        return ret

                
                
            
            

            
            




        
        