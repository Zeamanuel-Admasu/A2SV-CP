# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        A = 1
        flag = False
        for elem in s:
            if elem == "(":
                flag = True
                stack.append(elem)
            else:
                if flag:
                    score += 2**(len(stack) - 1)
                    flag = False
                stack.pop()
                
        return score
                
                
        