class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        low = 1;
        high = max_pile

        while (high > low):
            mid = (high + low) // 2
            speed = mid
            # mid is some speed that we will now test
            count = 0
            for pile in piles:
                count += math.ceil(pile / speed)
            if (count <= h):
                # this speed works, but lets try to find a slower speed
                # that can still work
                high = mid
            else:
                # this speed is too slow
                low = mid + 1

        return low
                