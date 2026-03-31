class Solution:
    def rob(self, nums: List[int]) -> int:
        [2, 9, 8, 3, 6]

        # only one house
        if len(nums) == 1:
            return nums[0]

        # two houses 
        if len(nums) == 2:
            return max (nums[0], nums[1])

        maxs = max(nums[len(nums) - 1], nums[len(nums) - 2]);
        i = len(nums) - 3

        while i > -1:
            if i + 3 <= len(nums) - 1:
                nums[i] += max (nums[i + 2], nums[i + 3])
                maxs = max(nums[i], maxs)
            else: 
                nums[i] += nums[i + 2]
                maxs = max(maxs, nums[i])
            i -= 1

        return maxs



        