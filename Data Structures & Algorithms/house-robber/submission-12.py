class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def helper(index: int) -> int:
            if (index > len(nums) - 1):
                return 0
            if (memo[index] != -1):
                return memo[index]
            else:
                mem = max(nums[index] + helper(index + 2), helper(index + 1))
                memo[index] = mem
                return mem
        
        return helper(0)

        
        
            
        