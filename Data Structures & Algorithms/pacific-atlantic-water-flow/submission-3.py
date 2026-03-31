class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        def helper(grid: List[List[bool]]):
            while len(q) > 0:
                cell = q.popleft()
                row, col = cell[0], cell[1]
                grid[row][col] = True
                
                for direction in directions:
                    if row + direction[0] in range(len(heights)) and col + direction[1] in range(len(heights[0])):
                        if heights[row + direction[0]][col + direction[1]] >= heights[row][col]:
                            if grid[row + direction[0]][col + direction[1]] != True:
                                q.append((row + direction[0], col + direction[1]))

        atlantic = [[False] * len(heights[0]) for _ in range(len(heights))]
        pacific = [[False] * len(heights[0]) for _ in range(len(heights))]
        ret = []

        # for pacific, we look at the first row and first column 
        q = deque()
        for col in range(len(heights[0])):
            q.append((0, col))
        for row in range(len(heights)):
            q.append((row, 0))
        helper(pacific)
        q.clear()

        # for atlantic 
        for col in range(len(heights[0])):
            q.append((len(heights) - 1, col))
        for row in range(len(heights)):
            q.append((row, len(heights[0]) - 1))
        helper(atlantic)

        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if atlantic[row][col] and pacific[row][col]:
                    ret.append([row, col])
        
        return ret
        
        
        


            

                
        