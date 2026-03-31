class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s;
        
        longest = 0;
        ret = '';
        i = 0;
        
        while i < len(s):
            left = i - 1 
            right = i + 1
            length = 1;

            # odd palindromes only
            while (left > -1 and right < len(s)):
                if (s[left] == s[right]):
                    length += 2;
                    left -= 1;
                    right += 1;
                else: break;
            if length > longest:
                ret = s[(left + 1) : (right)];
                longest = length;
            
            # even palindromes
            left = i;
            right = i + 1;
            length = 0;
            while (left > -1 and right < len(s)):
                if (s[left] == s[right]):
                    length += 2;
                    left -= 1;
                    right += 1;
                else: break;
            if length > longest:
                ret = s[(left + 1) : (right)];
                longest = length;
            
            i += 1;

        return ret;




        