# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums):
        summ, minSum, maxSum = 0, 0, 0
        for num in nums:
            summ += num
            maxSum = max(maxSum, summ)
            minSum = min(minSum, summ)
        return abs(maxSum - minSum)