class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        farthest = 0
        for i in range(len(nums)):
            if i <= farthest:
                farthest = max(i + nums[i], farthest)
            if farthest >= target: return True

        return False

        
        