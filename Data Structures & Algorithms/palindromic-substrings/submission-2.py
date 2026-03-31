class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1;

        ret = 0;
        i = 0
        while i < len(s):
            ret += 1;
            left = i - 1;
            right = i + 1;

            while (left > -1 and right < len(s)):
                if (s[left] == s[right]):
                    left -= 1;
                    right += 1;
                    ret += 1;
                else: 
                    break;
            
            left = i;
            right = i + 1;
            while (left > -1 and right < len(s)):
                if (s[left] == s[right]):
                    left -= 1;
                    right += 1;
                    ret += 1;
                else: 
                    break;

            i += 1;

        return ret;


        