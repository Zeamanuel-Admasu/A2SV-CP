# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        dictt = {"L":"R", "R":"L"}
        stack = []
        stack.append(s[0])
        count = 0
        for i in range(1, len(s)):
            if stack and s[i] != stack[-1]:
                stack.pop()
                if not stack:
                    count += 1
            else:
                stack.append(s[i])
        return count
        