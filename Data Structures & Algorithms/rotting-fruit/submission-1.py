from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False] * COLS for _ in range(ROWS)]

        q = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited[i][j] = True
        def addOrange(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or visited[i][j] or grid[i][j] == 0:
                return
            q.append((i, j))
            visited[i][j] = True
        time = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                addOrange(i + 1, j)
                addOrange(i - 1, j)
                addOrange(i, j + 1)
                addOrange(i, j - 1)
            if q:
                time += 1
        for i in range(ROWS):
            for j in range(COLS):
                if not visited[i][j] and grid[i][j] != 0:
                    return -1
        return time
                