class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # first of all: we can ignore triplets that have a higher value
        # than the target triplet at any index. 
        # second: each possible triplet must have at least 1 of the three values
        # on target
        first, second, third = False, False, False
        for triplet in triplets:
            valid = True
            for i in range(len(triplet)):
                if triplet[i] > target[i]:
                    valid = False
            if not valid:
                continue
            if triplet[0] == target[0]:
                first = True
            if triplet[1] == target[1]:
                second = True
            if triplet[2] == target[2]:
                third = True
            if first and second and third:
                return True

        return False


        