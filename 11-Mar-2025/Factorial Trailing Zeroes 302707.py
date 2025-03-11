# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def factorial(self, n):
            if n == 1 or n == 0:
                return 1
            return n * factorial(n-1)
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        a = self.factorial(n)
        count = 0
        while a % 10 == 0:
            count += 1
            a = a //10
        return count
        # b = str(a)
        # count = 0
        # for i in b[::-1]:
        #     if i != "0":
        #         return count
        #     count += 1


        