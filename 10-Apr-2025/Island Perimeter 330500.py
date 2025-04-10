# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * len(grid[0]) for i in range(len(grid))]
        ans = 0
        def inbound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
        def dfs(grid, row, col, visited):
            nonlocal ans
            print(row , col)
            visited[row][col] = True
            for i, j in direction:
                nrow = row + i
                ncol = col + j
                if not inbound(nrow, ncol) or grid[nrow][ncol] == 0:
                    ans += 1
                else:
                    if inbound(nrow, ncol) and not visited[nrow][ncol] and grid[nrow][ncol] == 1:
                        dfs(grid, nrow, ncol, visited)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(grid, row, col, visited)
                    return ans
        
        