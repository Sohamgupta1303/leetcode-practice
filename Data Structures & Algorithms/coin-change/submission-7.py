class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # so we go through every amount from 1 - amt [ 1 - 12 ]
        # and for each amount we need to go through all of the 
        # coins and see which coins we can even use. Coins must
        # be less than or equal to the amount. 
        amt = 1
        while amt < amount + 1:
            amt_dp = amount + 1
            for coin in coins:
                # if coin is less than amount and dp[amount - coin]
                # has a value then we can update it. 
                if coin <= amt and dp[amt - coin] != amount + 1:
                    amt_dp = min(1 + dp[amt - coin ], amt_dp)
            dp[amt ] = amt_dp
            amt += 1

        if dp[amount ] == amount +1:
            return -1
        else: return dp[amount]



                

        