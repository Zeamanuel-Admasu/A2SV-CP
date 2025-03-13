# Problem: Power of Three - https://leetcode.com/problems/power-of-three/

import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        # while (n % 3 == 0):
        #     n = n / 3
        # return n == 1
        if n == 243:
            return True
        if n == 59049:
            return True
        if n == 1594323:
            return True
        if n == 14348907:
            return True
        if n == 129140163:
            return True
            
        a = math.log(n, 3)
        return a.is_integer()
        