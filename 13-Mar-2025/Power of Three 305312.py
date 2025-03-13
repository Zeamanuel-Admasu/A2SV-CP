# Problem: Power of Three - https://leetcode.com/problems/power-of-three/

import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        def helper(n):
            if n == 1:
                return True
            if n % 3 != 0 or n <= 0:
                return False
            if n % 3 == 0:
                return helper(n / 3)
        return helper(n)
        
        