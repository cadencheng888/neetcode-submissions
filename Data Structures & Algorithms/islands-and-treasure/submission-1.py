class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def addRoom(i, j):
            if (i < 0 or i == ROWS or j < 0 or j == COLS or visited[i][j] or grid[i] [j] == -1):
                return
            visited[i][j] = True
            q.append([i, j])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visited[i][j] = True
        dist = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = dist
                addRoom(i + 1, j)
                addRoom(i - 1, j)
                addRoom(i, j + 1)
                addRoom(i, j - 1)
            dist += 1