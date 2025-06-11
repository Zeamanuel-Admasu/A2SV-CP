# Problem: Non-Decreasing Subsequences - https://leetcode.com/problems/non-decreasing-subsequences/description/

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        final = []
        res = []
        def backtrack(idx):
            if len(res) >= 2:
                final.append(res[:])
            used = set()
            for i in range(idx, len(nums)):
                if (not res or nums[i] >= res[-1]) and nums[i] not in used:
                    used.add(nums[i])
                    res.append(nums[i])
                    backtrack(i + 1)
                    res.pop()
        backtrack(0)
        return final

        