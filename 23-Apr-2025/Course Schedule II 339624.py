# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]
        queue = deque()
        order = []

        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1
        
        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            order.append(course)
            for nbr in graph[course]:
                incoming[nbr] -= 1
                if incoming[nbr] == 0:
                    queue.append(nbr)
        if len(order) != numCourses:
            return []
        return order
            
        