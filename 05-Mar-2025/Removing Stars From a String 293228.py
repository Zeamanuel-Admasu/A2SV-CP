# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for element in s:
            
            if element == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(element)
        return "".join(stack)
        

        