class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # go through the values and edit the index of the value to be * -1 
        # keep going if the value is negative that value has been repeated

        for i in range (len(nums)):
            value = abs(nums[i])
            if nums[value] < 0:
                return value
            else:
                nums[value] = nums[value] * -1
        
        return -1


        

