# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        visited = set()
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    graph[i].append(j)

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        count = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                count += 1

        return count
