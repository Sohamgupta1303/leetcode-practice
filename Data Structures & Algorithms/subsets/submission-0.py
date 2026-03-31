class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        ret.append([])

        def helper(subset: List[int], index: int):
            if index == len(nums):
                return
            
            # if you dont decide to add this number
            # you dont have to append anything to ret, as 
            # the subset array should already be appended. 
            helper(subset, index + 1)

            # if you decide to add this number
            # you have to create a new array and append that to ret
            # then call helper with that new array
            sub = subset + [nums[index]]
            ret.append(sub)
            helper(sub, index + 1)
        
        helper([], 0)
        return ret

        