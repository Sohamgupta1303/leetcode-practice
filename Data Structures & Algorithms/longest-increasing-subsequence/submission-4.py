class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1] * len(nums)   

        for i in range(len(nums)):
            j = i - 1
            best = 0
            while j >= 0:
                if nums[j] < nums[i]:
                    best = max(best, memo[j])
                j -= 1
            memo[i] = best + 1
        
        return max(memo)
        

            








        