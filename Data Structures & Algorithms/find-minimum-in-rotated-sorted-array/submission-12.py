class Solution:
    def findMin(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0];
        low = 0;
        high = len(nums) - 1
        
        while (high > low):
            mid = (high + low) // 2
            if (nums[mid] > nums[high]):
                # on the right side
                low = mid + 1
                # on the left side, including mid
                # nums[mid] if less than leftmost value
                # or equal (only happens if low = mid)
            else:
                high = mid;
        return nums[low]
        

            
        