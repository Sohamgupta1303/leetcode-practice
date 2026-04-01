class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2**31 - 1
        q = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append((row, col))

        # queue now has all of the treasure chests
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:
            for i in range(len(q)):
                cell = q.popleft()
                row, col = cell[0], cell[1]

                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    if new_row in range(len(grid)) and new_col in range(len(grid[0])):
                        if grid[new_row][new_col] == inf:
                            grid[new_row][new_col] = 1 + grid[row][col]
                            q.append((new_row, new_col))
        

                        
                

        