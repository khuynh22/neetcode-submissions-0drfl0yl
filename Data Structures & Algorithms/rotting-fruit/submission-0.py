class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        time, fresh = 0, 0
        neighbors = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
                
        while queue and fresh > 0:
            len_q = len(queue)
            for i in range(len_q):
                r, c = queue.popleft()

                for dr, dc in neighbors: 
                    if r + dr in range(ROWS) and c + dc in range(COLS) and grid[r + dr][c + dc] == 1:
                        grid[r + dr][c + dc] = 2
                        fresh -= 1
                        queue.append((r + dr, c + dc))

            time += 1

        return time if fresh == 0 else -1
                
