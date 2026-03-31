class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []

        def helper(index: int, remaining: int, values: List[int]):
            if index == len(nums):
                return
            if remaining - nums[index] < 0:
                # dont keep the number:
                helper(index + 1, remaining, values)
                return 

            vals = []
            for val in values:
                vals.append(val)
            vals.append(nums[index])

            if remaining - nums[index] == 0:
                ret.append(vals)
                

            # keep the number:
            helper(index, remaining - nums[index], vals)

            # dont keep the number:
            helper(index + 1, remaining, values)

        helper(0, target, [])
        return ret