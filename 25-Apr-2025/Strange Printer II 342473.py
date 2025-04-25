# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        n , m = len(targetGrid), len(targetGrid[0])
        boundaries = defaultdict(lambda: [float('inf'), -1, float('inf'), -1])
        for r in range(n):
            for c in range(m):
                color = targetGrid[r][c]
                boundaries[color][0] = min(boundaries[color][0], c)
                boundaries[color][1] = max(boundaries[color][1], c)
                boundaries[color][2] = min(boundaries[color][2], r)
                boundaries[color][3] = max(boundaries[color][3], r)
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for color in boundaries:
            l, r, t, b = boundaries[color]
            graph[color]
            for sr in range(t, b + 1):
                for sc in range(l, r + 1):
                    newColor = targetGrid[sr][sc]
                    if newColor != color:
                        graph[color].append(newColor)
                        indegree[newColor] += 1
        print(graph)
        queue = deque()
        for node in graph:
            if indegree[node] == 0:
                queue.append(node)
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for nbr in graph[node]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    queue.append(nbr)
        return count == len(boundaries)
            




        