class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)

        def helper (index: int) ->int:
            if (index > len(cost) - 1):
                return 0

            if memo[index] != -1:
                return memo[index]
            else:
                mem = cost[index] + min(helper(index + 1), helper(index + 2))
                memo[index] = mem
                return mem
        
        return min(helper(0), helper(1))
            
        