class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = [([None] * len(heights[0])) for _ in range(len(heights))]
        atlantic = [([None] * len(heights[0])) for _ in range(len(heights))]

        def helper (q: deque, array: List[List[bool]]):
            while q:
                cell = q.popleft()
                if not array[cell[0]][cell[1]]:
                    array[cell[0]][cell[1]] = True
                    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
                    for direction in directions:
                        x = cell[0] + direction[0]
                        y = cell[1] + direction[1]
                        if x in range(len(heights)) and y in range(len(heights[0])):
                            if not array[x][y] and heights[x][y] >= heights[cell[0]][cell[1]]:
                                q.append((x, y))

        q = deque()
        for col in range(len(heights[0])):
            q.append((0, col))
        for row in range(len(heights)):
            q.append((row, 0))
        helper(q, pacific)

        q.clear()
        for col in range(len(heights[0])):
            q.append((len(heights) - 1, col))
        for row in range(len(heights)):
            q.append((row, len(heights[0]) - 1))
        helper(q, atlantic)

        ret = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if atlantic[row][col] and pacific[row][col]:
                    ret.append([row, col])
        
        return ret
        
        
        
        
                    

        

        


       
        
        
        


            

                
        