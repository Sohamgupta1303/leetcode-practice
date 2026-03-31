class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = [0] * (n + 1)
        for i in range(n + 1):
            # i is the number we are working with
            # like 0, 1, 2, 3, 4
            if i == 4: print("hi")
            res = i
            count = 0
            while (res != 0):
                count += 1
                res = res & (res - 1)
            ret[i] = count
        
        return ret

