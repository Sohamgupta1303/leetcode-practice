class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(left: int, right: int) -> str:
            while (left > -1 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1

            return s[left + 1: right]
        
        longest = ""
        for i in range(len(s)):
            odd = helper(i,i)
            even = helper(i, i + 1)

            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even
        
        return longest



        
        