class Solution:
    def countSubstrings(self, s: str) -> int:

        def helper(left: int, right: int) -> int:
            count = 0
            while (left > -1 and right < len(s) and s[left] == s[right]):
                count += 1
                left -= 1
                right += 1
            
            return count
        count = 0
        for i in range(len(s)):
            count += helper(i, i)
            count += helper(i, i+ 1)
        
        return count

        