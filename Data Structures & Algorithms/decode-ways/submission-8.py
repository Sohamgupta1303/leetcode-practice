class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1] * (len(s) + 1)
        memo[-1] = 1

        def helper(index: int) -> int:
            if index >= len(s):
                return 1
            if s[index] == "0":
                return 0
            
            if index < len(s) - 1 and int(s[index: index + 2]) < 27:
                if memo[index + 2] == -1:
                    memo[index + 2] = helper(index + 2)
                if memo[index + 1] == -1:
                    memo[index + 1] = helper(index + 1)
                return memo[index + 2] + memo[index + 1]
            
            if memo[index + 1] == -1:
                memo[index + 1] = helper(index + 1)
            return memo[index + 1]
        
        return helper(0)
        



        