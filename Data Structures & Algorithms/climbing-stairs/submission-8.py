class Solution:

    def climbStairs(self, nint: int) -> int:
        memo = [-1] * nint

        def helper(n: int) -> int:
            if n < 0:
                return 0
            if n == 0:
                return 1
            if memo[n - 1] != -1: 
                return memo[n-  1]
            else:
                memo[n - 1] = helper(n - 1) + helper(n - 2)
                return memo[n - 1]

        return helper(nint)
            
        