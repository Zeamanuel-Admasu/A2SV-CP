# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 1:
                return x
            if n == 0:
                return 1
            if n < 0:
                x = 1/x
                n = -n
            if n % 2 == 0:
                return helper((x ** (n / (n/2))), (n / 2))
            
            return x * helper(x, n - 1)
        
        return helper(x, n)
        
        