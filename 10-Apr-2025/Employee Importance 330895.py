# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        edge_list = {}
        for emp in employees:
            edge_list[emp.id] = (emp.importance, emp.subordinates)
        count = 0 
        def dfs(node_id):
            nonlocal count
            imp, subs = edge_list[node_id]
            count += imp
            for subs_id in subs:
                dfs(subs_id)
        dfs(id)
        return count
