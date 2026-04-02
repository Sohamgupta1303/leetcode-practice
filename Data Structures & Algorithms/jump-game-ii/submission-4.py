class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest = 0
        jumps = 0
        i = 0
        while i <= len(nums):
            # if the furthest we can go extends the last element
            # => termination case
            if furthest >= len(nums) - 1:
                return jumps
            
            # take the jump that gets you the furthest
            new_furthest = furthest
            while i <= furthest:
                new_furthest = max(new_furthest, i + nums[i])
                i += 1
            jumps += 1
            furthest = new_furthest
            

        return jumps


                

            

                
    
            




        