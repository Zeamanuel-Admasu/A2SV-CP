# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dictt = {0 : 1}
        res = 0
        currSum = 0
        for n in nums:
            currSum += n
            res += dictt.get(currSum - k, 0)
            dictt[currSum] = 1 + dictt.get(currSum, 0)
        return res
        