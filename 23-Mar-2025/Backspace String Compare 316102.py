# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for elem in s:
            if elem != "#":
                stack1.append(elem)
            elif stack1 and elem == "#":
                stack1.pop()
        for elem in t:
            if elem != "#":
                stack2.append(elem)
            elif stack2 and elem == "#":
                stack2.pop()
        if stack1 == stack2:
            return True
        return False

        