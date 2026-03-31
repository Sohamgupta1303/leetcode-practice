class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0]) # 1 - indexed

        low = 0;
        high = rows - 1

        while (high >= low):
            mid = (low + high) // 2
            # find the row that our target is in binarily
            if (matrix[mid][0] <= target and matrix[mid][cols - 1] >= target):
                col_low = 0
                col_high = cols - 1
                while (col_high >= col_low):
                    col_mid = (col_high + col_low) // 2
                    if (matrix[mid][col_mid] == target):
                        return True
                    elif (matrix[mid][col_mid] > target):
                        col_high = col_mid - 1
                    else:
                        col_low = col_mid + 1
                return False
            # if target is bigger than both values
            elif (matrix[mid][0] < target and matrix[mid][cols - 1] < target):
                low = mid + 1
            # if target less than both values
            else:
                high = mid - 1

        return False


        

        