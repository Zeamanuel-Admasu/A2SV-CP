# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def inbound(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS
        visited = set()
        def dfs(r, c):
            area = 1
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if inbound(nr, nc) and (nr, nc) not in visited and grid[nr][nc]:
                    area += dfs(nr, nc)
            return area
        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visited or grid[r][c] == 0:
                    continue
                area = dfs(r, c)
                max_area = max(max_area, area)
        return max_area


        