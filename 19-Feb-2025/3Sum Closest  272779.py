# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minim = float("inf")
        n = len(nums)
        for i in range(n-2):
            l  = i + 1
            r = n - 1
            while l < r:
                curr = nums[i]
                summ = curr + nums[l] + nums[r]
                if abs(summ - target) < abs(minim-target):
                    minim = summ
                if summ < target:
                    l += 1
                elif summ > target:
                    r -= 1
                else:
                    return summ
        return minim


            