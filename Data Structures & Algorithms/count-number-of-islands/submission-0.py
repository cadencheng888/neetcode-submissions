class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        neighbors = []
        def dfs(i, j):
            if visited[i][j] == True:
                return
            visited[i][j] = True
            if i + 1 < len(grid) and grid[i + 1][j] == "1":
                dfs(i + 1, j)
            if i - 1 > -1 and grid[i - 1][j] == "1":
                dfs(i - 1, j)
            if j + 1 < len(grid[0]) and grid[i][j + 1] == "1":
                dfs(i, j + 1)
            if j - 1 > -1 and grid[i][j - 1] == "1":
                dfs(i, j - 1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visited[i][j] == False:
                    count += 1
                    dfs(i, j)
        return count
        