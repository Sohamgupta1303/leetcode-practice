class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = 0
        sum = 0

        for num in nums:
            sum += num
            if sum < 0:
                sum = 0
            if sum > ret:
                ret = sum

        if ret == 0: return max(nums)
        return ret
            


        