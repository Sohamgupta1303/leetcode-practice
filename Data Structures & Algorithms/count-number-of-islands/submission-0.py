class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        
        def helper(row: int, col: int):
            if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0])):
                return
            if (row, col) not in visited and grid[row][col] == "1":
                visited.add((row, col))
            else:
                return
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for direction in directions:
                helper(row + direction[0], col + direction[1])
        
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == "1":
                    # we have not discovered this island
                    count +=1 
                    # mark contiguous pieces of land as visited
                    helper(row, col)

        return count
            

        