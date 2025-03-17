# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def fourthRoot(self, n):
        if n == 1:
            return True
        if n <= 0:
            return False
        if n % 4 != 0:
            return False
        
        return self.fourthRoot(n//4)

    def isPowerOfFour(self, n: int) -> bool:
        return self.fourthRoot(n)


        