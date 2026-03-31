class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        def helper(row: int, col: int) -> int:
            if (row < 0 or col < 0 or row > len(grid) - 1 or col > len(grid[0]) - 1):
                return 0
            if grid[row][col] != 1:
                return 0
            # the index is in range and a 1
            # lets mark it visited
            grid[row][col] = 0

            return 1 + helper(row -1, col) + helper(row + 1, col) + helper(row, col - 1)+ helper(row, col +1)
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    value = helper(row, col)
                    max_area = max(value, max_area)
        return max_area
        