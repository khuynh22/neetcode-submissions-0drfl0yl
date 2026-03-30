class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROW, COL = len(image), len(image[0])
        original_pixel = image[sr][sc]
        def dfs(image, r, c, visit):
            if (r >= ROW or c >= COL or min(r, c) < 0 or (r, c) in visit or image[r][c] != original_pixel):
                return
            visit.add((r, c))
            image[r][c] = color
            dfs(image, r + 1, c, visit)
            dfs(image, r - 1, c, visit)
            dfs(image, r, c + 1, visit)
            dfs(image, r, c - 1, visit)
            visit.remove((r, c))
        
            return
        dfs(image, sr, sc, set())
        return image
