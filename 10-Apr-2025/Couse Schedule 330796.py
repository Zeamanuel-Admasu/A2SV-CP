# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = defaultdict(list)
        for a, b in prerequisites:
            adj_list[a].append(b)
        white = 1
        grey = 2
        black = 3
        color = {k: white for k in range(numCourses)}
        no_cycle = True
        def dfs(node):
            nonlocal no_cycle
            if not no_cycle:
                return
            color[node] = grey
            if node in adj_list:
                for nbour in adj_list[node]:
                    if color[nbour] == white:
                        dfs(nbour)
                    elif color[nbour] == grey:
                        no_cycle = False
                        return
            color[node] = black
        for i in range(numCourses):
            if color[i] == white:
                dfs(i)
        return no_cycle
