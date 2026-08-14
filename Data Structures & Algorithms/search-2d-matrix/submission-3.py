class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS - 1

        while top <= bottom:
            current = (top + bottom) // 2
            if target > matrix[current][-1]:
                top = current + 1
            elif target < matrix[current][0]:
                bottom = current - 1
            else:
                break
        if not (top <= bottom):
            return False

        l, r = 0, COLS - 1
        print("hi")
        
        while l <= r:
            i = (l + r) // 2
            print(i)
            if matrix[current][i] > target:
                r = i - 1
                
                print(f"left update{l}, {i}")
            elif matrix[current][i] < target:
                print(f"right update{r}")
                l = i + 1
            else:
                return True
        return False
