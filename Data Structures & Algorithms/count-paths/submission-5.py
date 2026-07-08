class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m - 1][n - 1] = 1

        def dfs(x: int, y:int):
            if x not in range(0, m) or y not in range (0, n):
                return 
            
            if x + 1 in range (0, m):
                if dp[x + 1][y] != 0:
                    dp[x][y] += dp[x + 1][y]
                else:
                    dfs(x + 1, y)
                    dp[x][y] += dp[x + 1][y]
            
            if y + 1 in range (0, n):
                if dp[x][y + 1] != 0:
                    dp[x][y] += dp[x][y + 1]
                else:
                    dfs(x, y + 1)
                    dp[x][y] += dp[x][y + 1]
                    
        
        dfs(0, 0)
        return dp[0][0]
            
            

        
        
            
            
            
            

        
        