class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fruit = 0
        q = deque()
        arr = []
        visited = set()
        directions = ((1, 0), (-1, 0), (0, -1), (0, 1))
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fruit += 1
                if grid[row][col] == 2:
                    arr.append((row, col))

        q.append(arr)
        
        def helper() -> int:
            rotted_fruit = 0
            wave = 0
            while len(q) != 0:
                fruits = q.popleft()
                # termination cases
                if len(fruits) == 0:
                    if rotted_fruit == fruit:
                        return wave 
                    else:
                        return -1

                # regular case
                arr = []
                for f in fruits:
                    f_row = f[0]
                    f_col = f[1]
                    for direction in directions:
                        new_row = f_row + direction[0]
                        new_col = f_col + direction[1]
                        if (new_row > -1 and new_row < len(grid) and new_col > -1 and new_col <len(grid[0])
                            and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited):
                            visited.add((new_row, new_col))
                            rotted_fruit += 1
                            arr.append((f_row + direction[0], f_col + direction[1]))
                q.append(arr)
                if len(arr) > 0:
                    wave += 1
            
            return wave

        return helper()







            



        

