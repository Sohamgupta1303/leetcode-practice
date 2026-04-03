class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret = 0

        # for each num we want to see what the possible 
        # max and min up to that point are. 

        cur_max, cur_min = 1, 1
        for num in nums:
            old_cur_min = cur_min
            cur_min = min(num, cur_max * num, cur_min * num)
            cur_max = max(num, cur_max * num, old_cur_min * num)
            ret = max(cur_max, ret)
        
        if ret == 0:
            return max(nums)
        return ret



       