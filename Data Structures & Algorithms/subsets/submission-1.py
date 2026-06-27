class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def recurse (index: int, stack: List[int]):
            if index == len(nums):
                ret.append(stack.copy())
                return
            
            # now can either choose to inlcude or exclude this index
            stack.append(nums[index])
            recurse(index + 1, stack)
            stack.pop()
            recurse(index + 1, stack)
            
        recurse(0, [])
        return ret

        