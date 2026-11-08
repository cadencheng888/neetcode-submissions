class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        longestArea = 0
        current = 0
        def dfs(i, j):
            nonlocal current
            if visited[i][j]:
                return
            current += 1
            visited[i][j] = True
            if i + 1 < len(grid) and grid[i + 1][j] == 1:
                dfs(i + 1, j)
            if i - 1 > -1 and grid[i - 1][j] == 1:
                dfs(i - 1, j)
            if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                dfs(i, j + 1)
            if j - 1 > -1 and grid[i][j - 1] == 1:
                dfs(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == 1:
                    current = 0
                    dfs(i, j)
                    longestArea = max(current, longestArea)
        return longestArea
        
            
            