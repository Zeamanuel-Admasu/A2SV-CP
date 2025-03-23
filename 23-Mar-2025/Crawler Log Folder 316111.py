# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for elem in logs:
            if stack and elem == "../":
                stack.pop()
            elif elem == "./":
                continue
            elif elem != "../" and elem != "./":
                stack.append(elem)  
        return len(stack)     