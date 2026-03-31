class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        letters = set()
        for num in nums:
            if num in letters:
                return True
            letters.add(num)
            
        return False
