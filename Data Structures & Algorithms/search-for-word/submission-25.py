class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # outside of helper function we should go through
        # all the letters and call helper on each of them
        def helper (row: int, col: int, index: int, visited: Set[Tuple[int, int]]) -> bool:
            # the function terminates in 4 cases:
            # 1) the word is not made => we return false
            # 2) the word is made and finished
            # => board[row][col] == word[index] and 
            #    index = len(word) - 1.
            # 3) row or col are out of bounds
            # 4) we have been to this index before
            if (row < 0 or row >= len(board) or col < 0 or col >= len(board[0])):
                return False
            if (row, col) in visited:
                return False
            if (board[row][col] != word[index]):
                return False
            if (board[row][col] == word[index]):
                print(board[row][col])
                if index == len(word) - 1:
                    return True
                else: 
                    visited.add ((row, col))
                    result =  (helper(row + 1, col, index + 1, visited) or 
                                helper(row, col + 1, index + 1, visited) or
                                helper(row - 1, col, index + 1, visited) or 
                                helper(row, col - 1, index + 1, visited))
                    visited.remove((row, col))
                    return result


            # inside the helper funciton, we have to
            # make a recrusive call. There are 2 options 
            # we choose. We always consider the current 
            # letter, but we must choose between the letter
            # at row + 1 or col + 1. 

        visit = set()
        for row in range (len (board) ):
            for col in range (len (board[0])):
                if helper(row, col, 0, visit):
                    return True
                visit.clear()
        return False

        