class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[None] * len(word2) for _ in range(len(word1))]

        def recurse (left: int, right: int) -> int:
            # uneven lengths:
            if left >= len(word1) and right >= len(word2):
                return 0
            
            # word 1 shorter than word 2
            if left < len(word1) and right == len(word2):
                return len(word1) - left
            
            #word 1 bigger than word 2
            if left == len(word1) and right < len(word2):
                return len(word2) - right
            
            if dp[left][right] is not None:
                return dp[left][right]

            # no character diff
            if word1[left] == word2[right]:
                dp[left][right] = recurse(left + 1, right + 1)
                return dp[left][right]
            
            # character diff: 3 options
            else:
                delete_value = 1 + recurse(left + 1, right) 
                insert_value = 1 + recurse(left, right + 1)
                replace_value = 1 + recurse(left + 1, right + 1)
                dp[left][right] = min(delete_value, insert_value, replace_value)
                return dp[left][right]
            
        return recurse(0, 0)
            


        