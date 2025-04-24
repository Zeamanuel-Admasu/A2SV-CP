# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        order = []
        colors = [0 for _ in range(len(graph))]
        
        def dfs(node):
            if colors[node] == 1:
                return False
            colors[node] = 1
            for nbr in graph[node]:
                if colors[nbr] == 2:
                    continue
                if not dfs(nbr):
                    return False
            colors[node] = 2
            order.append(node)
            return True
        
        for node in range(len(graph)):
            if colors[node] != 0:
                continue
            dfs(node)
        
        order.sort()
        return order