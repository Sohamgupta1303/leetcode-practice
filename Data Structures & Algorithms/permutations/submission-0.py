class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def helper (visited: Set[int], permutation: List[int]):
            if len(permutation) == len(nums):
                ret.append(permutation)
            
            for num in nums:
                if num not in visited:
                    # 2 outputs: one where we keep num, and one where we dont
                    # lets say we keep it :
                    new_visited = visited.copy()
                    new_visited.add(num)
                    new_perm = permutation + [num]
                    helper(new_visited, new_perm)

                    # if we dont keep it, we gotta go to the next number 
                    # which will happen in the loop automatically
        
        visited = set()
        helper(visited, [])
        return ret

            

            
            
            
        