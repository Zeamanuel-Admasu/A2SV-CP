# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def backTrack(i):
            if len(path) == k:
                res.append(path[:])
                return 
            if i > n:
                return 
            
            path.append(i)
            backTrack(i + 1)

            path.pop()
            backTrack(i + 1)
            return res
        return backTrack(1)
        