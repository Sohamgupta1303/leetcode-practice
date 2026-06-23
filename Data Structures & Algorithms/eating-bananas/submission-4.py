class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # gives a bunch of piles
        # need to find the minumum rate to eat the bananas
        # such that it takes <= h hours 

        # the highest rate is max of the array (1 hour for each pile)
        # the lowest rate is 1, (piles[i] hours for each pile)
        # conduct binary search from 1 - max to find the lowest rate that works

        low = 1
        high = max(piles)
        mid = (high + low) // 2

        lowest = high

        while low < high:
            # check if mid works
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours <= h:
                lowest = min(mid, lowest)
                high = mid 
                mid = (low + high ) // 2
            else:
                low = mid + 1
                mid = (low + high ) // 2
        
        return lowest
            
