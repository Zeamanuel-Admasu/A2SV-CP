# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        colors = [0 for _ in range(numCourses)]
        order = []

        for node, pre in prerequisites:
            graph[pre].append(node)

        def dfs(node, colors, graph, order):
            if colors[node] == 1:
                return False
            colors[node] = 1
            for nbr in graph[node]:
                if colors[nbr] == 2:
                    continue
                if not dfs(nbr, colors, graph, order):
                    return False
            colors[node] = 2
            order.append(node)
            return True

        for node in range(numCourses):
            if colors[node] != 0:
                continue
            if not dfs(node, colors, graph, order):
                return []
       
        return list(reversed(order))
        
       