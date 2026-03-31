class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        def helper(self, x: int, y: int) -> int:
            # check if we are at the end
            if x == m - 1 and y == n - 1 :
                return 1;
            
            sum = 0;
            # check if not at end
            if (x >= m or y >= n):
                return 0;
            if (x + 1 < m):
                sum += helper(self, x + 1, y);
            if (y + 1 < n):
                sum += helper(self, x, y + 1);
            return sum;

        return helper(self, 0, 0);
            

    
        
        