# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:

        def partition(i, curr, target, string):
            if i == len(string) and curr == target:
                return True
            for j in range(i, len(string)):
                string[i:j + 1]
                if partition(j + 1, curr + int(string[i:j+1]), target, string):
                    return True
            return False
        res = 0
        for i in range(1, n + 1):
            if partition(0, 0, i, str(i * i)):
                res += i * i
        return res