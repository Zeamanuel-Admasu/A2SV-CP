# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            return "".join("1" if c == "0" else "0" for c in s)
        def helper(n):
            if n == 1:
                return "0"
            s = helper(n-1) + "1" + "".join(reversed(invert(helper(n-1))))
            return s
        string = helper(n)
        return string[k-1]
            

        