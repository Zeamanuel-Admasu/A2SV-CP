# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        j1 = 0
        curSum1 = 0
        total1 = 0
        for i in range(len(nums)):
            curSum1 += nums[i]
            while curSum1 > goal:
                # print("aa",nums[j1:i])
                curSum1 -= nums[j1]
                j1 += 1
            total1 += i - j1 + 1
        if goal == 0:
            return total1
                # print(nums[j1:i])
        j2 = 0
        curSum2 = 0 
        total2 = 0
        for i in range(len(nums)):
            curSum2 += nums[i]
            while curSum2 > (goal-1):
                curSum2 -= nums[j2]
                j2 += 1
            total2 += i - j2 + 1
            # print(curSum1, nums[j1:i+1])
        
            
        return total1 - total2

        