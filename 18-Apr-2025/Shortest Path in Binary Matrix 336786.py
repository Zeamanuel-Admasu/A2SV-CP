# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        queue = deque([(0, 0, 1)])
        visited = set((0, 0))
        
        while queue:
            row, col, length = queue.popleft()
            if grid[row][col] == 1:
                continue
            if row == len(grid) - 1 and col == len(grid) - 1 :
                return length
            for i, j in directions:
                nr = row + i
                nc = col + j
                if 0 <= nr < len(grid) and 0 <= nc < len(grid) and (nr, nc) not in visited and grid[nr][nc] == 0:
                    visited.add((nr, nc))
                    queue.append((nr, nc, length + 1))
        return -1