class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_val = nums[0]

        for i in range(len(nums)):
            soFar = nums[i]
            max_val = max(max_val, soFar)
            j = i + 1
            while j < len(nums):
                soFar *= nums[j]
                max_val = max(max_val, soFar)
                j += 1
        
        return max_val
        