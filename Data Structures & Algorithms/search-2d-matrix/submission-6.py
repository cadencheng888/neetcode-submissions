class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first search the cols to see in which row it lies
        # then search that row
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS - 1
        row = 0
        while bottom >= top:
            row = (top + bottom) // 2
            if matrix[row][0] <= target <= matrix[row][COLS - 1]:
                break
            elif target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][COLS - 1]:
                top = row + 1

        left, right = 0, COLS - 1
        while left <= right:
            m = (left + right) // 2
            print(left, right, m)
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                left = m + 1
            else:
                right = m - 1
        return False 