# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations):
        if not citations: return 0
        n = len(citations)
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end)//2
            if mid + citations[mid] >= n:
                end = mid - 1
            else:
                start = mid + 1                
        return n - start