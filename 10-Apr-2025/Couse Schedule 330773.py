# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj_list[a].append(b)
        white = 1
        grey = 2
        black = 3
        Color = {k: white for k in range(numCourses)}
        no_cycle = True
        def dfs(node):
            nonlocal no_cycle
            if not no_cycle:
                return
            Color[node] = grey
            for nbour in adj_list[node]:
                if Color[nbour] == white:
                    dfs(nbour)
                elif Color[nbour] == grey:
                    no_cycle = False
                    return
            Color[node] = black
            
        
        for i in range(numCourses):
            if Color[i] == white:
                dfs(i)
        return no_cycle

        