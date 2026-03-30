class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        def dfs(grid, r, c):
            if min(r, c) < 0 or r >= ROW or c >= COL or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)
        
        count = 0 
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    count += 1
                    dfs(grid, r, c)
        
        return count