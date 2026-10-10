class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        def dfs(i, j, length):
            if length == len(word):
                return True
            if (i < 0 or i >= ROWS or j < 0 or j >= COLS or visited[i][j] == True or word[length] != board[i][j]):
                return False
            visited[i][j] = True
            result = dfs(i + 1, j, length + 1) or dfs(i - 1, j, length + 1) or dfs(i, j + 1, length + 1) or dfs(i, j - 1, length + 1)
            visited[i][j] = False
            return result
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        return False
