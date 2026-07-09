class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1] * len(text2) for _ in range(len(text1))]
        def recurse (index1: int, index2: int) -> int:
            if index1 == len(text1) or index2 == len(text2):
                return 0
            if dp[index1][index2] > -1:
                return dp[index1][index2]
            if text1[index1] == text2[index2]:
                dp[index1][index2] = (1 + recurse(index1 + 1, index2 + 1))
                return dp[index1][index2]
            else:
                dp[index1][index2] = max(recurse(index1 + 1, index2), 
                                        recurse(index1, index2 + 1))
                return dp[index1][index2]
        
        return recurse(0, 0)


        

