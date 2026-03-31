class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        q = deque()
        
        directions = ((1, 0), (-1, 0), (0, -1), (0, 1))
        def helper():
            while q:
                cell = q.popleft()
                row, col = cell[0], cell[1]
                board[row][col] = "T"

                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    if new_row in range(rows) and new_col in range(cols) and board[new_row][new_col] == "O":
                        q.append((new_row, new_col))

            q.clear()

        for col in range(cols):
            if board[0][col] == "O":
                q.append((0, col))
                helper()
            if board[rows - 1][col] == "O":
                q.append((rows - 1, col))
                helper()
        
        for row in range(rows):
            if board[row][0] == "O":
                q.append((row, 0))
                helper()
            if board[row][cols - 1] == "O":
                q.append((row, cols - 1))
                helper()
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "T":
                    board[row][col] = "O"
            

        

        


            
        
            

        