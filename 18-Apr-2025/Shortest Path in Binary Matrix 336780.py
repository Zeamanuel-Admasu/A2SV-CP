# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [1, -1], [-1, 1], [1, 1]]
        if grid[0][0] == 1:
            return -1
        queue = deque()
        queue.append([0, 0, 1])
        visited = set((0, 0))
        while queue:
            row, col, length = queue.popleft()
            if row == len(grid) - 1 and col == len(grid) - 1:
                return length
            for i, j in directions:
                nr, nc = row + i, col + j
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != 1 and (nr, nc) not in visited:
                    visited.add((nr, nc)) 
                    queue.append([nr, nc, length + 1])   
        return -1    
                