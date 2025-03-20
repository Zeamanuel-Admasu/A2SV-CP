# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        res = []
        def backtrack(idx):
            if idx >= len(s):
                for i in range(1, len(res)):
                    if res[i - 1] - res[i] != 1:
                        return False
                return len(res) >= 2
            
            for i in range(idx, len(s)):
                val = int(s[idx:i+1])
                if res and res[-1] - val != 1:
                    continue
                res.append(val)
                if backtrack(i + 1):
                    return True
                res.pop()
            return False
        return(backtrack(0))