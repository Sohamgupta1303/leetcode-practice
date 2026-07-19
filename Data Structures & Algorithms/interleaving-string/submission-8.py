class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = [[None] * len(s2) for _ in range(len(s1))]

        def recurse (s3_index: int, s1_index: int, s2_index: int) -> bool:
            if s3_index == len(s3):
                return s1_index == len(s1) and s2_index == len(s2)

             # if not computed, calculate and store. 
            if s1_index == len(s1):
                return s3[s3_index:] == s2[s2_index:]
            
            if s2_index == len(s2):
                return s3[s3_index:] == s1[s1_index:]

            # if already computed before
            if dp[s1_index][s2_index] is not None:
                return dp[s1_index][s2_index]
            
           

            # s3 char == s1 char == s2 char
            if s3[s3_index] == s1[s1_index] and s3[s3_index] == s2[s2_index]:
                left = recurse(s3_index + 1, s1_index + 1, s2_index) 
                right = recurse (s3_index + 1, s1_index, s2_index + 1)
                dp[s1_index][s2_index] = left or right
                return dp[s1_index][s2_index]
            
            if s3[s3_index] == s1[s1_index]:
                return recurse(s3_index + 1, s1_index + 1, s2_index) 
            
            if s3[s3_index] == s2[s2_index]:
                return recurse (s3_index + 1, s1_index, s2_index + 1)
            
            return False

        return recurse (0, 0, 0)
            




