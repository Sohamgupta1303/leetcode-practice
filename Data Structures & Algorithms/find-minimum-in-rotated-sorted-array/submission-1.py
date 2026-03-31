class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
        middle = 0
        mini = float('inf')
        
        while (left != right):
            middle = (int) ((left + right)/2)
            if nums[middle] > nums[left]:
                left = middle;
                mini = min(mini, nums[middle])
            else:
                mini = min(mini, nums[middle])
                right = middle

        return min(nums[0], mini)
                



