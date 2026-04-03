class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # first of all: we can ignore triplets that have a higher value
        # than the target triplet at any index. 
        # second: each possible triplet must have at least 1 of the three values
        # on target
        first, second, third = False, False, False
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            if a == target[0]:
                first = True
            if b == target[1]:
                second = True
            if c == target[2]:
                third = True
            if first and second and third:
                return True

        return False


        