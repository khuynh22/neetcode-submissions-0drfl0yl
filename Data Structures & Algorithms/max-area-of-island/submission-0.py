class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        def dfs(grid, r, c):
            if r >= ROW or c >= COL or min(r, c) < 0 or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            return 1 + dfs(grid, r + 1, c) + dfs(grid, r - 1, c) + dfs(grid, r, c + 1) + dfs(grid, r, c - 1)

        area = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    area = max(area, dfs(grid, r, c))
            
        return area

