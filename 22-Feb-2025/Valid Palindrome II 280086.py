# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        print(Counter(s))
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                skipL, skipR = s[i + 1:j + 1], s[i:j]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            i += 1
            j -= 1
        return True
    