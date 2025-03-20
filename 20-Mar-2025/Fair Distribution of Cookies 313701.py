# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child = [0] * k
        self.res = float("inf")
        self.n = len(cookies)
        def backtrack(i, child):
            if i == self.n:
                self.res = min(self.res, max(child))
                return 

            
            for j in range(k):
                child[j] += cookies[i]
                backtrack(i + 1, child)
                child[j] -= cookies[i]
                if child[j] == 0:
                    break
        backtrack(0, child)
        return self.res
                # if child[]

        