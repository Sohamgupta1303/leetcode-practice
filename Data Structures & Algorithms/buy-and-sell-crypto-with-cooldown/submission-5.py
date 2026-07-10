class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[None] * 2 for _ in range(len(prices))] 

        def recurse (index: int, bought: int) -> int:
            if index >= len(prices):
                return 0
            if dp[index][bought] is not None:
                return dp[index][bought]
            if not bought:
                dp[index][bought] =  max (prices[index] * -1 + recurse(index + 1, 1), 
                    recurse(index + 1, 0))
            else:
                dp[index][bought] =  max(prices[index] + recurse (index + 2, 0), 
                            recurse (index + 1, 1))

            return dp[index][bought] 

        return recurse(0, 0)
        
