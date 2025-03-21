# Problem: Replace the Substring for Balanced String - https://leetcode.com/problems/replace-the-substring-for-balanced-string/

class Solution:
    def balancedString(self, s: str) -> int:
        dictt = Counter(s)
        print(dictt)
        l = 0
        minim = len(s)
        if all(dictt[v] == len(s)//4 for v in "QWER"):
            return 0
        for r in range(len(s)):
            dictt[s[r]] -= 1
            while l <= r and all(dictt[v] <= (len(s) // 4) for v in "QWER"):
                minim = min(minim, r - l + 1)
                dictt[s[l]] += 1
                l += 1 
            
        return minim
            
            
        
        