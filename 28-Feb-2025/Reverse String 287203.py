# Problem: Reverse String - https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = len(s) - 1
        for i in range(len(s) // 2):
            s[i], s[j] = s[j], s[i]
            j -= 1
        return s

        