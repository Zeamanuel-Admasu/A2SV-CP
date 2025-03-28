# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        


        def recursion(s):
            if len(s) <= 1:
                return ""
            count = Counter(set(s))
            for i in range(len(s)):
                if s[i].islower():
                    if s[i].upper() in count:
                        continue
                    else:
                        left = recursion(s[:i])
                        right = recursion(s[i+1:])
                    if len(left) < len(right):
                        return right
                    else:
                        return left
                elif s[i].isupper():
                    if s[i].lower() in count:
                        continue
                    else:
                        left = recursion(s[:i])
                        right = recursion(s[i+1:])
                    if len(left) < len(right):
                        return right
                    else:
                        return left
            return s
        return recursion(s)
            
        
        
        




        

        