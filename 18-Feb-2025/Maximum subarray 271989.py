# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxim = nums[0]
        nums[0] = max(0,nums[0])
        for i in range(1, len(nums)):
            if nums[i] + nums[i - 1] < 0:
                maxim = max(maxim,nums[i])
            nums[i] += nums[i-1]

            if nums[i] < 0:
                nums[i] = 0
            else:
                maxim = max(maxim,nums[i])
        
        return maxim


        