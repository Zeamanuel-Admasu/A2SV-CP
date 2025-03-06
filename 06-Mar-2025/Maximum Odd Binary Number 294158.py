# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        a = Counter(s)
        length = sum(a.values())
        res = ""
        while a["1"] != 1:
            res += "1"
            a["1"] -= 1
        while a["0"] != 0:
            res += "0"
            a["0"] -= 1
        
        res += "1"
        print(res)
        return res

