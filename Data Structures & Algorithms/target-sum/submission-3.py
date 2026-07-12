class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [-1] * len(nums) 

        def recurse (index: int, sum: int) -> int:
            if index == len(nums) and sum == target:
                return 1
            if index == len(nums):
                return 0
        
            return recurse(index + 1, sum + nums[index]) + recurse(index + 1, sum - nums[index])
            
            #return dp[index]
        
        return recurse(0, 0)


        