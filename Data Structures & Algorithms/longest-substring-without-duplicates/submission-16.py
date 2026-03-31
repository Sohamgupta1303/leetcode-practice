class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        characters = set();
        left = 0
        right = 0
        longest = 0
        currLen = 0
        while (right < len(s)):
            if (s[right] not in characters):
                characters.add(s[right]);
                right += 1;
                currLen += 1;
                longest = max(currLen, longest);
            else:
                characters.remove(s[left]);
                left += 1;
                currLen -= 1

        return longest;



        