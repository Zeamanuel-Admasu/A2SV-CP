# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        print(paths)
        stack = []
        for element in paths:
            if element == '':
                continue
            else:
                if stack and element == "..":
                    stack.pop()
                elif element == ".":
                    continue
                elif element != "..":
                    stack.append(element)
        return "/" + "/".join(stack)
                    
            
            
        #     if path == ".." and stack:
        #         stack.pop()
        #     elif path != "" and path != ".":
        #         stack.append()
                

        