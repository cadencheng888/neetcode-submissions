class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        def backtrack(i, j, index):
            if index == len(word):
                return True
            if (i < 0 or i >= ROWS or j < 0 or j >= COLS
            or visited[i][j] == True or word[index] != board[i][j]):
                return False
            visited[i][j] = True
            res = (backtrack(i + 1, j, index + 1) or backtrack(i - 1, j, index + 1)
            or backtrack(i, j + 1, index + 1) or backtrack(i, j - 1, index + 1))
            visited[i][j] = False
            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, 0):
                    return True
        return False
            