# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shifted = [0] * (len(s) + 1)
        
        
        for l, r, d in shifts:
            if d:
                shifted[l] += 1
                shifted[r+1] -= 1
            else:
                shifted[l] -= 1
                shifted[r+1] += 1
        pref = [0] * len(s)
        pref[0] = shifted[0]
        for i in range(1, len(s)):
            pref[i] = pref[i-1] + shifted[i]
        arr = []
        for i in s:
            arr.append((ord(i) - 97))
        for i in range(len(arr)):
            pref[i] = (pref[i] + arr[i]) % 26 
            pref[i] += 97
            pref[i] = chr(pref[i])
        return "".join(pref)
        

        
